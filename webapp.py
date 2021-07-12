from http.server import BaseHTTPRequestHandler, HTTPServer
class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write("Hello SCRIBERTECH".format(self.path).encode('utf-8'))
def run(server_class=HTTPServer, handler_class=Server, port=80):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
run()
