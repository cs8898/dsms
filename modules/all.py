from config import config


def handle(json_conf):
    if len(config.HOSTS) is None:
        return {'ok': True, 'message': 'No Hosts', 'endpoint': 'all'}
    ret = {'ok': True, 'endpoint': 'all'}
    for host in config.HOSTS:
        ret[host.name] = host.do_endpoints()
        if not ret[host.name]['ok']:
            ret['ok'] = False
    return ret
