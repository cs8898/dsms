import json
import os


def handle(config):
    conf = json.loads(config)
    processes = []
    if conf is not None:
        if len(conf) > 0:
            processes = conf
    alive = []

    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    for pid in pids:
        try:
            cmdline = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read().split(b'\0')
            cmdline = list(map(lambda x: x.decode('UTF-8'), cmdline))
            for term in processes:
                found = False
                for cmdpart in cmdline:
                    if cmdpart.endswith(term):
                        found = True
                        break
                if found and alive.count(term) == 0:
                    alive.append(term)
        except IOError:  # proc has already terminated
            continue
    for term in alive:
        processes.remove(term)
    dead = processes
    return {'ok': len(dead) == 0, 'alive': alive, 'dead': dead, 'endpoint': 'processes'}
