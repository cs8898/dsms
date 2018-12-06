from dsmsMods.config import config
from . import host
from emoji import emojize
import json
from os.path import isfile


def load_hosts():
    hosts = []
    conf = {}
    if isfile(config.DSMS_FILE):
        conf = json.load(open(config.DSMS_FILE))
    if "hosts" in conf:
        print(emojize(":card_index: loading hosts"))
        for entry in conf['hosts']:
            hosts.append(
                host.host_from_dict(entry)
            )
            hosts[len(hosts) - 1].print()
    return hosts


def load_config():
    conf = {}
    if isfile(config.DSMS_FILE):
        conf = json.load(open(config.DSMS_FILE))
    if "config" in conf:
        print(emojize(":card_index: loading config"))
        for entry in conf['config']:
            if "port" == entry:
                config.DSMS_PORT = conf['config']['port']
