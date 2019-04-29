#!python3

from http.server import BaseHTTPRequestHandler
from pathlib import Path
from subprocess import Popen, PIPE

def getOutput(cmd):
    stdout = Popen(cmd, shell=True, stdout=PIPE).stdout
    output = stdout.read()
    output = output.decode('utf-8')
    return output

routes = {
    '/' : 'Buehl - ITS_5900 Advanced Final\n\nPages:\n- ifconfig\n- ps\n- ls',
    '/ifconfig' : getOutput('ifconfig'),
    '/ps' : getOutput('ps'),
    '/ls' : getOutput('ls')
}

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return
        
    def do_POST(self):
        return

    def do_GET(self):
        self.respond()

    def handle_http(self):
        status = 200
        content_type = 'text/plain'
        
        if self.path in routes:
            response_content = routes[self.path]
        else:
            status = 404
            response_content = '404 Page Not Found!!'

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(response_content, 'UTF-8')


    def respond(self):
        content = self.handle_http()
        self.wfile.write(content)