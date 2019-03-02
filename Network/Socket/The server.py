import socket
s = socket.socket()

host = '127.0.0.1'
port = 1234
s.bind((host, port))

s.listen(5)
while True:
   c, addr = s.accept()
   print('Got connection from', addr)
   c.send('Thank you for connecting'.encode())   # python3.5和Python2.7在套接字返回值解码上有区别。
                                                 # 需要用encode()方法将str转换为bytes
   c.close()