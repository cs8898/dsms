import json
import shutil

GIGABYTE = 1073741824


def handle(config):
    conf = json.loads(config)
    path = '/'
    scale = GIGABYTE
    minimum = GIGABYTE
    if conf is not None:
        if "path" in conf:
            path = conf['path']
        if "scale" in conf:
            scale = conf['scale']
        if "minimum" in conf:
            minimum = conf['minimum']*scale
    free = shutil.disk_usage(path).free
    return {'ok': free >= minimum, 'free': shutil.disk_usage(path).free / scale, 'endpoint': 'diskspace'}
