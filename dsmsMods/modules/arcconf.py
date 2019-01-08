# import json
import os

ARCCONF_CMD = 'arcconf LIST 1'


def handle(json_conf):
    # conf = json.loads(json_conf)
    arcconf_output = os.popen(ARCCONF_CMD).read()
    logicaldisks = arcconf_parser(arcconf_output)
    res = {'ok': True, 'logicaldisks': logicaldisks, 'endpoint': 'arcconf'}
    for ld in logicaldisks:
        if "Optimal" not in logicaldisks[ld]:
            res['ok'] = False
    return res


def arcconf_parser(arcconf_output):
    state = 0
    output = arcconf_output.split('\n')
    raids = {}
    for line in output:
        if state == 0 and line.startswith("---"):
            state = 1
        elif state == 1 and line.startswith("Logical device information"):
            state = 12
        elif state == 1 and not line.startswith("Logical device information"):
            state = 2
        elif state == 2 and line.startswith("---"):
            state = 3
        elif state == 3 and line.startswith(" "):
            state = 4
        elif state == 4 and line.startswith("---"):
            state = 5
        elif state == 5 and line == "":
            state = 0
        elif state == 5:
            #BODY
            state = 5
        elif state == 12 and line.startswith("---"):
            state = 13
        elif state == 13 and line.startswith(" "):
            state = 14
        elif state == 14 and line.startswith("---"):
            state = 15
        elif state == 15 and line == "":
            state = 0
        elif state == 15:
            # BODY
            rname = line.split(':')[1].split(')')[1].strip(' ')
            raids[rname] = line.split(':')[1].split('(')[0].strip(' ')
    return raids
