#!python3

from http.server import HTTPServer
import time
from buehl_server import Server


HOST_NAME = 'localhost'
PORT_NUMBER = 8080

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))