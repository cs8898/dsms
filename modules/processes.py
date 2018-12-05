import json
import os


def handle(config):
    conf = json.loads(config)
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    for pid in pids:
        try:
            print("TODO")
            # print(pid)
            # print(open(os.path.join('/proc', pid, 'cmdline'), 'rb').read().split(b'\0'))
        except IOError:  # proc has already terminated
            continue
    return "processes"
