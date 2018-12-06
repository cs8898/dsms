import json
from config import config
import logic.host


def handle(json_conf):
    conf = json.loads(json_conf)
    testhost = None
    if len(conf) > 0:
        print(conf)
        testhost = logic.host.host_from_dict(conf)
    else:
        for host in config.HOSTS:
            if host.name == 'localhost':
                testhost = host
                break
    if testhost is None:
        testhost = logic.host.Host('localhost', 'localhost')
    ret = testhost.do_endpoints()
    ret['endpoint'] = 'health'
    return ret
