import sys
sys.path.append("../")
import random
import requests
from logging_service import config

users = [
    {"user_id": 123,"vendor_id": 345},
    {"user_id": 456,"vendor_id": 345}
]
pages = [
    {"url": "http://page1.com", "query": "apple=123&banana=456"},
    {"url": "http://page2.com", "query": "pizza=123&party=456"}
]
events = [
    {"category": "Analytics Overview", "action": "Calendar Clicked", "label": "1 Month", "value": 1},
    {"category": "Analytics Overview", "action": "Calendar Clicked", "label": "3 Month", "value": 3},
    {"category": "Analytics Details", "action": "Thingy Clicked", "label": "Thingy", "value": {"apple": 123}}
]
contexts = [
    {"apple": 123, "orange": 456},
    {"banana": 3424, "pizza": 245435},
    {"pizza": 34234, "party": 3424}
]
# endpoints = ['syslog', 'page', 'event']

def _get_random_log():
    endpoint = random.choice(endpoints)
    # endpoint = "syslog"
    url = 'http://{host}:{port}/{endpoint}'.format(
        host = config.host,
        port = config.port,
        endpoint = endpoint)
    params = ''
    data = {
        "user": random.choice(users),
        "message": "default message",
        "context": {
            "apple": 123,
            "orange": 456
        }
    }

    if endpoint == "syslog":
        params = {"level": random.choice([
            'DEBUG',
            'INFO',
            'WARNING',
            'ERROR',])}

    if endpoint == "page":
        data = {
            "user": random.choice(users),
            "page": random.choice(pages),
            "context": random.choice(contexts)
        }
    if endpoint == "event":
        data = {
            "user": random.choice(users),
            "event": random.choice(events),
            "context": random.choice(contexts)
        }

    return (url, params, data)


for x in range(0, 3):
    (url, params, data) = _get_random_log()
    import pdb; pdb.set_trace()
    resp = requests.post(
        url,
        params=params,
        json=data)
