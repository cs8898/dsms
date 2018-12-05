import json
import shutil

GIGABYTE = 1073741824

def handle(config):
    conf = json.loads(config)
    return str(shutil.disk_usage('/').free/GIGABYTE)
