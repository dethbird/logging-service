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
 * Running on http://localhost:5008/ (Press CTRL+C to quit)
```

## check

use a service like curlbuilder to send logging commands to your logging service

#### /syslog

```bash
# INFO
curl -v -XPOST -H "Content-type: application/json" -d '{"user": {"vendor_id": 345, "user_id": 123}, "context": {"orange": 456, "apple": 123}, "message": "default message"}' 'http://localhost:5008/syslog?level=INFO'
```

#### /page

```bash
curl -v -XPOST -H "Content-type: application/json" -d '{"user": {"vendor_id": 345, "user_id": 456}, "page": {"url": "http://page2.com", "query": "pizza=123&party=456"}, "context": {"party": 3424, "pizza": 34234}}' 'http://localhost:5008/page'
```

#### /event

```bash
curl -v -XPOST -H "Content-type: application/json" -d '{"context": {"party": 3424, "pizza": 34234}, "user": {"vendor_id": 345, "user_id": 123}, "event": {"action": "Calendar Clicked", "value": 1, "category": "Analytics Overview", "label": "1 Month"}}' 'http://localhost:5008/event'
```

#### /tail


```bash
# tail 50 lines of logs
curl -v -H "Content-type: application/json" 'http://localhost:5008/tail?n=50'
```

#### Hello

```bash
# tail 50 lines of logs
curl -v -H "Content-type: application/json" 'http://localhost:5008/hello'
```

## apache proxy

make logging service available as vhost by using a configuration like this in your `vhost.conf`:

```bash
<VirtualHost 192.168.31.41:80>
        ServerName logging-service-dev.company.com
    ProxyPassMatch    ^ http://localhost:5008
    ProxyPassReverse  ^ http://localhost:5008
</VirtualHost>
```
