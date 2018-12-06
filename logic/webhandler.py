from http.server import BaseHTTPRequestHandler
from config import config
from platform import node
import modules
from modules import *
from urllib.parse import urlparse, unquote
import json


class Webhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(404)
            self.end_headers()
            return
        for module in modules.__all__:
            url = urlparse(self.path)
            json_obj = {}
            if len(url.query) > 0:
                json_obj = json.loads(unquote(url.query))
            if url.path[1:] == module:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('DSMS_Module', module)
                self.send_header('DSMS_Version', config.DSMS_VERSION)
                self.send_header('Hostname', node())
                self.end_headers()
                self.wfile.write(str.encode(json.dumps(
                    eval("modules.{}.handle(\'{}\')".format(module, json.dumps(json_obj)))
                ), 'UTF-8'))
                return
        self.send_error(404, "Not Found {}".format(self.path))

    def log_request(self, code='-', size='-'):
        return
