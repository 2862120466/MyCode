import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 建立连接:
''' 服务器的地址和端口 '''
host = '169.254.6.166'
port = 1234
clientsocket.connect((host, port))

# 接收欢迎消息:
print(clientsocket.recv(1024).decode('utf8')) # 接收小于 1024 字节的数据

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    clientsocket.send(data)
    print(clientsocket.recv(1024).decode('utf-8'))

clientsocket.send(b'exit')
clientsocket.close()