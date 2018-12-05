import requests
from requests import RequestException
from config import *
from emoji import emojize
from termcolor import colored


class Host:
    name = ""
    host = ""
    endpoints = []
    config = {}

    def __init__(self, name, host, endpoints=None, config=None):
        if endpoints is None:
            endpoints = []
        if config is None:
            config = {}
        self.name = name
        self.host = host
        self.endpoints = endpoints
        self.config = config

    def ping(self):
        try:
            r = requests.get("http://{}:{}/ping".format(self.host, self.config.get("port", DSMS_PORT)))
            return r.status_code == 200
        except RequestException:
            return False

    def print(self):
        up = self.ping()
        print("{} {}".format(
            emojize(colored(":thumbs_up: UP", 'green') if up else colored(":thumbs_down: DOWN", 'red')),
            self.name))
        print(" Endpoints:")
        for endpoint in self.endpoints:
            print("    {}".format(endpoint))

        print(" Config:")
        for conf in self.config:
            print("    {}: {}".format(conf, self.config[conf]))
