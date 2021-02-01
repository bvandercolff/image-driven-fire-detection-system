from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    messagetosend = bytes(('There is a fire, remain calm & get to safety.' if 2 % 2 == 0 else 'There is no fire'),"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    return


server_address_httpd = ('10.1.3.108',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('starting server')
httpd.serve_forever()
