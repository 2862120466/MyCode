from tkinter import Tk, Label,Button, StringVar
from tkinter import BOTTOM, TOP, RIGHT, BOTH, END
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

class Connector():
    global output, input
    members_check = 'accept_2862120466'
    socket_count = 1

    @classmethod
    def link_to_server(self):
        try:
            if Connector.socket_count:
                self.client_socket = socket(AF_INET, SOCK_STREAM)
                self.client_socket.connect(('169.254.6.166', 1234))
                self.client_socket.setblocking(False)
                self.socket_count -= 1
            else:
                showinfo("警告！！！", "不能再创建连接了")

            # msg_welcome = self.client_socket.recv(10240)
            # output.insert(END,'\n' + msg_welcome.decode())
        except:
            showinfo("警告！！！", "连接失败")

    def send_input(self):
        try:
            self.client_socket.send(input.get('1.0',END).strip().encode())
            input.delete('1.0', END)
        except:
            showinfo("警告！！！", "与服务器没有连接")

    # def read_data(self):
    #     try:
    #         self.msg = self.client_socket.recv(10240)
    #         return self.msg
    #     except:pass

    def recv_msg(self):
        try:
            self.msg = self.client_socket.recv(10240)
            print('recv from server:', self.msg.decode())

            if self.msg.decode()[0:17] != Connector.members_check:
                output.insert(END, '\n'*2 + self.msg.decode())
            else:
                members_name.set(self.msg.decode()[17:-1])

            top.after(2000, Connector().recv_msg)

        except:
            top.after(2000, Connector().recv_msg)

    def close(self):
        try:
            self.client_socket.send('close'.encode())
            output.insert(END, '\n' + '成功断开连接')

            self.client_socket.close()
            Connector.socket_count += 1
        except:
            showinfo("警告！！！", "与服务器没有连接")


    def clear_input(self):
        input.delete('1.0', END)

    def clear_output(self):
        output.delete('1.0', END)



top = Tk()
top.title('wcc的聊天室')
top.geometry("800x600")


members_name = StringVar()
members_name.set('无成员')


members = Label( textvariable=members_name,
                 font=('楷体', 14),
                 width=10)
members.pack(side=RIGHT,
             fill='y',
             )



input = ScrolledText(font='楷体',
                     height=5) # 输入区域
input.pack(side=BOTTOM)

output = ScrolledText(font=('楷体', 14),height=50,) # 聊天区域
output.pack(side=RIGHT,
            expand=True,
            fill=BOTH )


submit = Button(members,
                text='发送',
                font=('楷体',14),
                height=2,
                width=10,
                activebackground='gray',
                command=Connector().send_input)
submit.pack(side=BOTTOM)

reset = Button(members,
               text='重置',
               font=('楷体',14),
               height=2,
               width=10,
               activebackground='gray',
               command=Connector().clear_input)
reset.pack(side=BOTTOM)

link = Button(members,
                text='连接服务器',
                font=('楷体',14),
                height=1,
                width=10,
                activebackground='gray',
                command=Connector().link_to_server)
link.pack(side=TOP)

close = Button(members,
                text='断开连接',
                font=('楷体',14),
                height=1,
                width=10,
                activebackground='gray',
                command=Connector().close)
close.pack(side=TOP)


clear_output_button = Button(output,
                             text='clear',
                             font=('楷体', 10),
                             width=10,
                             activebackground='gray',
                             command=Connector().clear_output)
clear_output_button.pack(side=BOTTOM)

top.after(0,Connector().recv_msg)

top.mainloop() # 这是一个无限循环,显示主窗口