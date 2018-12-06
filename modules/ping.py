import json


def handle(config):
    conf = json.loads(config)
    res = {'ok': True, 'pong': 'pong', 'endpoint': 'ping'}
    if conf is not None and "pong" in conf:
        res['pong'] = conf['pong']
    return res
