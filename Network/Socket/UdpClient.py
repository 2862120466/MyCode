import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    clientsocket.sendto(data, ('169.254.6.166', 1234))
    # 接收数据:
    print((clientsocket.recv(1024)).decode())

clientsocket.close()