import requests
from requests import RequestException
import json


def dorequest(site):
    try:
        res = requests.get(site['url'])
        r = True
        if 'code' in site:
            r = res.status_code == site['code']
        if 'body' in site:
            r = site['body'].encode('UTF-8') in res.text.encode('UTF-8')
        return r
    except RequestException:
        return False


def handle(json_conf):
    conf = json.loads(json_conf)
    res = {'ok': True, 'correct': [], 'incorrect': [], 'endpoint': 'request'}
    sites = []
    if len(conf) > 0 and 'sites' in conf:
        sites = conf['sites']
    for site in sites:
        if dorequest(site):
            res['correct'].append(site['url'])
        else:
            res['ok'] = False
            res['incorrect'].append(site['url'])

    return res
