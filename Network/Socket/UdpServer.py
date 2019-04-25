import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serversocket.bind(('169.254.6.166', 1234))

 # 与TCP不同的是UDP连接不需要建立连接

while True:
    clientsocket, addr = serversocket.recvfrom(1024)
    print('Received from %s:%s.' % addr)

    serversocket.sendto( ('Hello, %s!' % clientsocket.decode() ).encode(), addr)