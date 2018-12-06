import json
import os
import re

MEMORY_CMD = "free | tail -n +2"


def handle(config):
    conf = json.loads(config)
    memory = os.popen(MEMORY_CMD).read().split("\n")
    memory = memory[:-1]
    memory = list(map(lambda x: re.split(" +", x), memory))
    memory = list(map(lambda x: [x[0][:-1].lower(), x[1], x[3]], memory))
    mems = {}
    for mem in memory:
        mems[mem[0]] = {'total': mem[1], 'free': mem[2]}

    return {'ok': True, 'memory': mems, 'endpoint': 'memory'}
