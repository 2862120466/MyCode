from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

client_socket_queue = []
members = 'accept_2862120466'

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('169.254.6.166',1234))

server_socket.listen(5)

user_dict = {
    '169.254.6.166':'TGW',
}

def send_msg(send_str):
    for client_socket in client_socket_queue:
        client_socket.send(send_str)

def tcplink(client_socket, addr):
    # client_socket.send('你成功加入聊天室！\n'.encode())
    # print("发送消息：'你成功加入聊天室！'给：%s:%s" % addr)

    while True:
        try:
            msg = client_socket.recv(10240)
            send_str = (user_dict.get(addr[0], ' ') + '：' + msg.decode()).encode()
            if msg.decode() == 'close':
                print("recv：%s" % msg.decode())

                members_new = members.replace( user_dict.get(addr[0]), '' )
                send_msg(members_new.encode())
                client_socket_queue.remove(client_socket)
                client_socket.close()

                print('关闭与%s:%s的连接' % addr)
                break

            elif msg.decode() and msg.decode() != 'close':
                print("recv：%s" % msg.decode())
                send_msg(send_str)
                print('send：%s' % msg.decode())

        except:
            break


while True: # 循环等待连接
    try:
        client_socket, addr = server_socket.accept()
        print('已与%s:%s创建连接' % addr)

        members += user_dict.get(addr[0]) + '\n'
        client_socket_queue.append(client_socket)
        send_msg(members.encode())

        t = Thread(target=tcplink, args=(client_socket, addr))
        t.start()
    except:
        break