from http.server import ThreadingHTTPServer

from config import config
from .webhandler import Webhandler
from termcolor import colored
from emoji import emojize
import threading


class Webserver(threading.Thread):
    server = None

    def run(self):
        self.server = ThreadingHTTPServer(('', config.DSMS_PORT), Webhandler)
        print(emojize(":rocket: starting webserver on {}".format(
            colored("http://{}:{}".format(self.server.server_address[0], self.server.server_port), 'blue')
        )))
        self.server.serve_forever()

    def stop(self, signum = None, frame = None):
        print(colored(emojize("\n:stop_sign: stopping webserver"), 'red'))
        self.server.shutdown()


def startserver():
    server = Webserver()
    server.start()
    return server


def stopserver(server=None):
    if server is not None:
        server.stop()
