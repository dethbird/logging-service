# logging-service
Flask based logging service

# setup and run


## python environment and packages

cd into the directory then setup python environment.

```bash
pyvenv env
```

activate that environment

```bash
source env/bin/activate
```

pip install required packages

```bash
pip install -r requirements.txt
```

## .env variables

setup your environment variables. copy `.env.shadow` to `.env` and put in your own parameters

```bash
cp .env.shadow .env
```

## run

```bash
python service.py
```

you should see the output (with your LOGGING_SERVICE_HOST and LOGGING_SERVICE_PORT env vars):

```bash
 * Running on http://localhost:514/ (Press CTRL+C to quit)
```

## check

use a service like curlbuilder to send logging commands to your logging service

#### /syslog

```bash
# INFO
curl -v -XPOST -H "Content-type: application/json" -d '{"user": {"vendor_id": 345, "user_id": 123}, "context": {"orange": 456, "apple": 123}, "message": "default message"}' 'http://localhost:514/syslog?level=INFO'
```

#### /page

```bash
curl -v -XPOST -H "Content-type: application/json" -d '{"user": {"vendor_id": 345, "user_id": 456}, "page": {"url": "http://page2.com", "query": "pizza=123&party=456"}, "context": {"party": 3424, "pizza": 34234}}' 'http://localhost:514/page'
```

#### /event

```bash
curl -v -XPOST -H "Content-type: application/json" -d '{"context": {"party": 3424, "pizza": 34234}, "user": {"vendor_id": 345, "user_id": 123}, "event": {"action": "Calendar Clicked", "value": 1, "category": "Analytics Overview", "label": "1 Month"}}' 'http://localhost:514/event'
```

#### /tail


```bash
# tail 50 lines of logs
curl -v -H "Content-type: application/json" 'http://localhost:514/tail?n=50'
```

#### Hello

```bash
# tail 50 lines of logs
curl -v -H "Content-type: application/json" 'http://localhost:514/hello'
```

## apache proxy

make logging service available as vhost by using a configuration like this in your `vhost.conf`:

```bash
<VirtualHost 192.168.XXX.XXX:80>
        ServerName logging-service.company.com
    ProxyPassMatch    ^ http://localhost:514
    ProxyPassReverse  ^ http://localhost:514
</VirtualHost>
```

## ngrok

```bash
wget ngrok_2.0.19_linux_386.zip

unzip ngrok_2.0.19_linux_386.zip

mv ngrok /usr/bin/

ngrok http 514

```
