from socketserver import TCPServer,StreamRequestHandler

class Handler(StreamRequestHandler):

   def handle(self):
       addr = self.request.getpeername()
       print('Got connection from', addr)
       self.wfile.write('Thank you for connecting'.encode())

server = TCPServer(('127.0.0.1', 1234), Handler)
server.serve_forever()