from tkinter import *

# 要创建GUI，可创建一个将充当主窗口的顶级组件（控件）。为此，可实例化一个Tk对象
top = Tk()

# 创建按钮（控件)，使用Button类实例化对象，但这个按钮现在是不可见的
# 控件包含各种属性，我们可以使用它们来修改控件的外观和行为
btn = Button()

def clicked():
    print('I was clicked!')
btn.config( text='Button', command=clicked )

# btn['text'] = 'this a button'
# btn['command'] = clicked #  在控制台打印消息



# 使用布局管理器来告诉Tkinter控件的位置，使其显示出来
btn.pack(anchor='e') # 使用pack()管理器,如果没有指定父控件(可使用构造函数的第一个可选参数)，默认主窗口为父控件

Label(text="I'm in the first window!").pack() # 用构造函数来配置控件
second = Toplevel() # Toplevel类表示除主窗口外的另一个顶级窗口，而Label就是文本标签
Label( second, text="I'm in the second window!" ).pack()


#  主事件循环，让窗口持续绘制，而不是直接退出
mainloop()


help(Pack.config)