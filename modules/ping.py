import json


def handle(config):
    conf = json.loads(config)
    if conf is not None and "pong" in conf:
        return conf["pong"]
    return "pong"
