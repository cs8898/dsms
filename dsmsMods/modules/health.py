import json
from dsmsMods.config import config
import dsmsMods.logic.host


def handle(json_conf):
    conf = json.loads(json_conf)
    testhost = None
    if len(conf) > 0:
        print(conf)
        testhost = dsmsMods.logic.host.host_from_dict(conf)
    else:
        for host in config.HOSTS:
            if host.name == 'localhost':
                testhost = host
                break
    if testhost is None:
        testhost = dsmsMods.logic.host.Host('localhost', 'localhost')
    ret = testhost.do_endpoints()
    ret['endpoint'] = 'health'
    return ret
