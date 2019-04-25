import socket

ip_port = ('127.0.0.1', 8009)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print('receive:', data.decode())

    inp = input('please input:')
    sk.sendall(inp.encode())

    if inp == 'exit':
        break

sk.close()