import json


def handle(config):
    conf = json.loads(config)
    return "memory"
