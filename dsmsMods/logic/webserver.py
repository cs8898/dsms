from http.server import HTTPServer
from socketserver import ThreadingMixIn

from dsmsMods.config import config
from .webhandler import Webhandler
from termcolor import colored
from emoji import emojize
import threading
import ssl


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

    def __init__(self, port, handler):
        super().__init__(port, handler)
        if config.DSMS_PEM != '':
            self.socket = ssl.wrap_socket(self.socket, certfile=config.DSMS_PEM, server_side=True)


class Webserver(threading.Thread):
    server = None

    def run(self):
        self.server = ThreadedHTTPServer(('', config.DSMS_PORT), Webhandler)
        print(emojize(":rocket: starting webserver on {}".format(
            colored("{}://{}:{}".format('http' if config.DSMS_PEM == '' else 'https',
                                        self.server.server_address[0],
                                        self.server.server_port), 'blue')
        )))
        self.server.serve_forever()

    def stop(self, signum=None, frame=None):
        print(colored(emojize("\n:stop_sign: stopping webserver"), 'red'))
        self.server.shutdown()


def startserver():
    server = Webserver()
    server.start()
    return server


def stopserver(server=None):
    if server is not None:
        server.stop()
