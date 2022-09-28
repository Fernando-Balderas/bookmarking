import json


def post_json(client, url, payload):
    return client.post(url, data=json.dumps(payload), content_type="application/json")


def put_json(client, url, payload):
    return client.put(url, data=json.dumps(payload), content_type="application/json")


def to_json(data):
    return json.loads(data.decode("utf-8"))
