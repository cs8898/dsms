from config import *
from host.host import Host
from emoji import emojize
import json


def load():
    hosts = []
    config = json.load(open(DSMS_FILE))
    print(emojize(":card_index: loading hosts"))
    for entry in config['hosts']:
        hosts.append(Host(entry, config['hosts'][entry]['host'],
                          config['hosts'][entry].get('endpoints', []), config['hosts'][entry].get('config', {})))
        # print("    {}: {}".format(
        #     hosts[len(hosts)-1].name,
        #     emojize(":thumbs_up: UP" if hosts[len(hosts)-1].ping() else ":thumbs_down: DOWN"))
        # )
        hosts[len(hosts)-1].print()
    return hosts
