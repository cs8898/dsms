import json
from dsmsMods.config import config
import dsmsMods.logic.host


def handle(json_conf):
    conf = json.loads(json_conf)
    testhost = None
    if len(conf) > 0:
        testhost = dsmsMods.logic.host.host_from_dict(conf)
    if testhost is None:
        for host in config.HOSTS:
            if host.host == 'localhost' or host.host == '127.0.0.1':
                print("Found LocalHOST")
                testhost = host
                break
    if testhost is None:
        testhost = dsmsMods.logic.host.Host('localhost', 'localhost')
    ret = testhost.do_endpoints()
    ret['endpoint'] = 'health'
    return ret
