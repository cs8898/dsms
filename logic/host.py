import requests
from requests import RequestException
from config import config
from emoji import emojize
from termcolor import colored
import json


class Host:
    name = ""
    host = ""
    endpoints = []
    conf = {}

    def __init__(self, name, host, endpoints=None, conf=None):
        if endpoints is None:
            endpoints = []
        if conf is None:
            conf = {}
        self.name = name
        self.host = host
        self.endpoints = endpoints
        self.conf = conf

    def do_endpoint(self, endpoint="ping"):
        try:
            conf = json.dumps(self.conf.get(endpoint, ""))
            r = requests.get("http://{}:{}/{}{}".format(
                self.host,
                self.conf.get('port', config.DSMS_PORT),
                endpoint,
                "" if len(conf) == 0 else '?' + conf
            ))
            if r.status_code == 200:
                return json.loads(r.content.decode('UTF-8'))
            else:
                return {'ok': False, 'code': r.status_code}
        except RequestException:
            return {'ok': False}

    def do_endpoints(self):
        endpoints = self.endpoints.copy()
        results = {'ok': True}
        if "ping" not in endpoints:
            endpoints.append("ping")
        for endpoint in endpoints:
            results[endpoint] = self.do_endpoint(endpoint)
            if not results[endpoint]['ok']:
                results['ok'] = False
        return results

    def ping(self):
        return self.do_endpoint()['ok']

    def print(self):
        up = self.ping()
        print("{} {}".format(
            emojize(colored(":thumbs_up: UP", 'green') if up else colored(":thumbs_down: DOWN", 'red')),
            self.name))
        print(" Endpoints: {}".format(json.dumps(self.endpoints)))
        print(" Config:")
        for conf in self.conf:
            print("    {}: {}".format(conf, json.dumps(self.conf[conf])))


def host_from_dict(host_dict):
    return Host(host_dict.get('name', host_dict['host']),
                host_dict['host'],
                host_dict.get('endpoints', []),
                host_dict.get('config', {}))
