from settings import *
from http.server import HTTPServer, BaseHTTPRequestHandler
from HTTP_request import HttpWorker


def run():
    """ Function for start server """
    httpd = HTTPServer((SERVER_NAME, SERVER_PORT), HttpWorker)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
