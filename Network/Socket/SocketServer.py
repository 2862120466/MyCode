from socketserver import TCPServer,StreamRequestHandler,ThreadingMixIn

#利用ThreadingMixIn类实现线程化，达到多个客户端同时连接
class Server(ThreadingMixIn,TCPServer):pass

#StreamRequestHandler负责在使用完连接后将其关闭
class Handler(StreamRequestHandler):

    def handle(self):
        #获取客户端套接字
        addr = self.request.getpeername()
        print('Got connection from',addr)
        #想客户端发送信息
        self.wfile.write('Thank you for your connecting'.encode())

#绑定IP+协议+端口，用来唯一标识一个进程
server = TCPServer(('127.0.0.1',1234),Handler)
server.serve_forever()
