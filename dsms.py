#!/usr/bin/env python3
from termcolor import colored, cprint
from config import config
from logic import *
import argparse
import time
import signal
import modules


def init(args=None):
    cprint(config.DSMS_TEXT, 'green')
    print('Version: {} by {}'.format(colored(config.DSMS_VERSION, 'green'), colored(config.DSMS_DEVELOPER, 'red')))
    print('Available Modules: {}\n'.format(colored(repr(modules.__all__), 'yellow')))
    config.set_config_file(args)
    loader.load_config()
    config.set_other_args(args)
    server = webserver.startserver()
    signal.signal(signal.SIGINT, server.stop)
    signal.signal(signal.SIGTERM, server.stop)

    time.sleep(1)
    hosts = loader.load_hosts()
    config.set_hosts(hosts)


parser = argparse.ArgumentParser(description="Dead Simple Monitoring Solution")
parser.add_argument("-c", help="Config File [{}]".format(config.DSMS_FILE), default="", type=str,
                    metavar="config")
parser.add_argument("-p", help="Listen Port [{}]".format(config.DSMS_PORT), default=-1, type=int,
                    metavar="port")
my_args = parser.parse_args()
init(my_args)
