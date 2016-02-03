from flask import Flask
from flask import request
from flask import Response
import logging
import loggly.handlers
import json
import time
import subprocess
from logging_service import config

# configure logger
logger = logging.getLogger(config.logging_service_name)
logger.setLevel(logging.DEBUG)

# stream handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# file handler
ch = logging.FileHandler(config.output_file)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# loggly handler
if config.loggly_uri != "":
    ch = loggly.handlers.HTTPSHandler(config.loggly_uri, 'POST')
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


# segment handler

def _format(logtype, request):
    """Converts an HTTP POST request to a log message

    Args:
        data: (JSON): JSON data to be formatted

    Returns:
        str: newly formatted log line with additional info.
    """

    data = request.json
    data['type'] = logtype
    data['timestamp'] = time.time()
    data['logger'] = logger.name
    data['app'] = app.name

    return json.dumps(data, sort_keys=True)


#create app
app = Flask(config.app_name)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS"
    response.headers['Access-Control-Allow-Headers'] = "Content-type"

    return response

@app.route('/syslog', methods=['POST'])
def syslog():
    """Log as system log

    """
    level = logging.DEBUG

    if request.args['log_level'] != None:
        level = config.logging_levels[request.args['log_level']]
    message = _format(syslog.__name__, request)
    logger.log(level, message)
    return Response(response=message,
                    status=200,
                    mimetype="application/json")

@app.route('/page', methods=['POST'])
def page():
    """Log as page view

    """
    level = logging.INFO
    message = _format(page.__name__, request)
    logger.log(level, message)
    return Response(response=message,
                    status=200,
                    mimetype="application/json")

@app.route('/event', methods=['POST'])
def event():
    """Log as clientside event

    """
    level = logging.INFO
    message = _format(event.__name__, request)
    logger.log(level, message)
    return Response(response=message,
                    status=200,
                    mimetype="application/json")


@app.route('/tail', methods=['GET'])
def tail():
    num = 100
    grep = None
    if request.args:
        if request.args['n']:
            num = request.args['n']
        # @todo(dethbird) add grep option
        # if request.args['grep']:
        #     grep = request.args['grep']

    proc = subprocess.Popen(["tail", "-n{num}".format(num=num), config.output_file], stdout=subprocess.PIPE)
    output = proc.stdout.read()
    output = output.decode("utf-8").rstrip('\n').split('\n')
    output.reverse()
    output = '[{output}]'.format(output=','.join(output))
    return Response(response=output,
                    status=200,
                    mimetype="application/json")

@app.route('/hello', methods=['GET'])
def hello():
    return Response(response=json.dumps({
        "host": config.host,
        "port": config.port,
        "ngrok_url": config.ngrok_url,
        "ngrok_monitor_url": config.ngrok_monitor_url,
        "message": "hello"}), status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
