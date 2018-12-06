from config import config


def handle(json_conf):
    hosts = []
    for host in config.HOSTS:
        hosts.append(host.__dict__)
    return {'ok': True, 'hosts': hosts}
