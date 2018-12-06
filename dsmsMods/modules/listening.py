import json
import os
import re

TCP_CMD = 'netstat -an | grep -i "LISTEN "'
UDP_CMD = 'netstat -an | grep -i udp'


def handle(config):
    conf = json.loads(config)
    tcp_search = []
    udp_search = []
    if conf is not None and len(conf) > 0:
        for elem in conf:
            if elem == 'udp':
                udp_search = conf['udp']
            elif elem == 'tcp':
                tcp_search = conf['tcp']
    tcp_ports = os.popen(TCP_CMD).read().split("\n")
    tcp_ports = list(map(lambda x: re.split(" +", x), tcp_ports))
    tcp_ports = list(filter(lambda x: len(x) >= 4, tcp_ports))
    tcp_ports = list(map(lambda x: int(re.split(":+", x[3])[1]), tcp_ports))
    udp_ports = os.popen(UDP_CMD).read().split("\n")
    udp_ports = list(map(lambda x: re.split(" +", x), udp_ports))
    udp_ports = list(filter(lambda x: len(x) >= 4, udp_ports))
    udp_ports = list(map(lambda x: int(re.split(":+", x[3])[1]), udp_ports))

    tcp_ok = []
    for tcp_port in tcp_ports:
        if tcp_port in tcp_search:
            tcp_ok.append(tcp_port)
            tcp_search.remove(tcp_port)
    udp_ok = []
    for udp_port in udp_ports:
        if udp_port in udp_search:
            udp_ok.append(udp_port)
            udp_search.remove(udp_port)
    return {'ok': len(tcp_search) == 0 and len(udp_search) == 0,
            'tcp': {'listen': tcp_ok, 'closed': tcp_search},
            'udp': {'listen': udp_ok, 'closed': udp_search},
            'endpoint': 'listening'}
