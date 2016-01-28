from flask import Flask
from flask import request
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
ch = loggly.handlers.HTTPSHandler(config.loggly_uri, 'POST')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

import pdb; pdb.set_trace()


# segment handler

def _format(level, data):
    """Converts an HTTP POST request to a log message

    Args:
        data: (JSON): JSON data to be formatted

    Returns:
        str: newly formatted log line with additional info.
    """
    # import pdb; pdb.set_trace()
    data['time'] = time.time()
    data['loggerName'] = logger.name
    data['appName'] = app.name
    return json.dumps(data, sort_keys=True)


#create app
app = Flask(config.app_name)

@app.route('/syslog', methods=['POST'])
def syslog():
    """Log as system log

    """
    level = logging.DEBUG
    if request.args['level'] != None:
        level = config.logging_levels[request.args['level']]

    message = _format(level, request.json)
    logger.log(level, message)
    return message

@app.route('/pageview', methods=['POST'])
def syslog():
    """Log as page view

    """
    level = logging.INFO
    message = _format(level, request.json)
    logger.log(level, message)
    return message

@app.route('/event', methods=['POST'])
def syslog():
    """Log as clientside event

    """
    level = logging.INFO
    message = _format(level, request.json)
    logger.log(level, message)
    return message


@app.route('/tail', methods=['GET'])
def tail():
    num = 100
    if request.args['n'] != None:
        num = request.args['n']

    proc = subprocess.Popen(["tail", "-n{num}".format(num=num), config.output_file], stdout=subprocess.PIPE)
    output = proc.stdout.read()
    return output

if __name__ == '__main__':
    app.run(host=config.host, port=config.port)