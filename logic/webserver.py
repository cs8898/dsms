from http.server import HTTPServer

from config import *
from .webhandler import Webhandler
from termcolor import colored
from emoji import emojize
import threading


class Webserver(threading.Thread):
    server = None

    def run(self):
        self.server = HTTPServer(('', DSMS_PORT), Webhandler)
        print(emojize(":rocket: starting webserver on {}".format(
            colored("http://{}:{}".format(self.server.server_address[0], self.server.server_port), 'blue')
        )))
        self.server.serve_forever()


def startserver():
    server = Webserver()
    server.start()
    return server
