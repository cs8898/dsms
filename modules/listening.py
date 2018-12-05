import json
import os
import re

TCP = 'netstat -an | grep -i "LISTEN "'
UDP = 'netstat -an | grep -i udp'


def handle(config):
    conf = json.loads(config)
    tcp_ports = os.popen(TCP).read().split("\n")
    tcp_ports = list(map(lambda x: re.split(" +", x), tcp_ports))
    tcp_ports = list(filter(lambda x: len(x) >= 4, tcp_ports))
    tcp_ports = list(map(lambda x: int(x[3].split(":")[1]), tcp_ports))
    udp_ports = os.popen(UDP).read().split("\n")
    udp_ports = list(map(lambda x: re.split(" +", x), udp_ports))
    udp_ports = list(filter(lambda x: len(x) >= 4, udp_ports))
    udp_ports = list(map(lambda x: int(x[3].split(":")[1]), udp_ports))
    return json.dumps([tcp_ports, udp_ports])
