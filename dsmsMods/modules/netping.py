import json
from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call  # Execute a shell command
import os
import re
import socket

"""simple Regex for DomainNames"""
HOST_RE = r"^[\w\-_]+(?:[.][\w\-_]+)*$"


def check_v6(host):
    try:
        socket.inet_pton(socket.AF_INET6, host)
        return True
    except:
        return False


def check_v4(host):
    try:
        socket.inet_pton(socket.AF_INET, host)
        return True
    except:
        return False


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    if not (check_v4(host) or check_v6(host) or re.search(HOST_RE, host, re.MULTILINE)):
        return False
    # Ping command count option as function of OS
    param = '-n' if system_name().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    # /dev/null to hide output
    fnull = open(os.devnull, 'w')

    # Pinging
    r = system_call(command, stdout=fnull, stderr=fnull)
    fnull.close()
    return r == 0


def handle(json_conf):
    conf = json.loads(json_conf)
    hosts = []
    res = {'ok': True, 'up': [], 'down': [], 'endpoint': 'netping'}
    if len(conf) > 0 and 'hosts' in conf:
        hosts = conf['hosts']
    for host in hosts:
        if ping(host):
            res['up'].append(host)
        else:
            res['ok'] = False
            res['down'].append(host)
    return res
