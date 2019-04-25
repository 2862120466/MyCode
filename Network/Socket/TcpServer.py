import socket
import threading
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建一个基于IPv4和TCP协议的Socket

# 获取本地主机名
host = socket.gethostname()
print('Wcc Server IP : %s'%host)
# 设置端口号
port = 1234
serversocket.bind((host, port)) # 端口绑定

serversocket.listen(5) # 对端口进行监听,设置最大连接数，超过后排队
print('Waiting for connection')


def tcplink(clientsocket, addr):
   print('Accept new connection from %s:%s' % addr)
   clientsocket.send('This is Wcc Server'.encode())

   while True:
      data = clientsocket.recv(1024)
      time.sleep(1)
      if not data or data.decode('utf-8') == 'exit':
         break
      clientsocket.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8')) # python3.5和Python2.7在套接字返回值解码上有区别,需要用encode()方法将str转换为bytes

   clientsocket.close()
   print('Connection from %s:%s closed.' % addr)


while True:
   clientsocket, addr = serversocket.accept() # accept()会等待并返回一个客户端的连接

   # 创建新线程来处理TCP连接:
   t = threading.Thread(target=tcplink, args=(clientsocket, addr))
   t.start()