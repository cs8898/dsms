from dsmsMods.config import config


def hash(ret):
    ret['hash'] = int(ret['ok'])
    temp = dict(sorted(ret.items(), key=lambda x: x[0]))
    for key in temp:
        if key is 'hash' or key is 'endpoint' or key is 'ok':
            continue
        print(key)
        ret['hash'] = ret['hash'] << 1
        ret['hash'] += int(temp[key]['ok'])
        temp[key] = dict(sorted(temp[key].items(), key=lambda x: x[0]))
        for subkey in temp[key]:
            if subkey is 'endpoint' or subkey is 'ok':
                continue
            print("    {}".format(subkey))
            ret['hash'] = ret['hash'] << 1
            ret['hash'] += int(temp[key][subkey]['ok'])
    return ret


def handle(json_conf):
    if len(config.HOSTS) is None:
        return {'ok': True, 'message': 'No Hosts', 'endpoint': 'all'}
    ret = {'ok': True, 'endpoint': 'all'}
    for host in config.HOSTS:
        ret[host.name] = host.do_endpoints()
        if not ret[host.name]['ok']:
            ret['ok'] = False
    ret = hash(ret)
    return ret
