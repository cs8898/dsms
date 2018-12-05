#!/usr/bin/env python3
from termcolor import colored, cprint
from config import *
from logic import *
import time

cprint(DSMS_TEXT, 'green')
print('Version: {} by {}\n'.format(colored(DSMS_VERSION, 'green'), colored(DSMS_DEVELOPER, 'red')))


def init():
    webserver.startserver()
    time.sleep(1)
    loader.load()


init()
