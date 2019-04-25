"""
要创建单行文本框，可使用控件Entry。
要创建可滚动的多行文本区域，可结合使用控件Text和Scrollbar，但模块tkinter.scrolledtext已经提供了一种实现。
要提取Entry控件的内容，可使用其方法get。

对于ScrolledText对象，我们将使用其方法delete和insert来删除文本。
调用方法delete和insert时，需要使用合适的参数来指定文本的位置；
'1.0'：来指定第1行的第0个字符（即第一个字符前面），
END：来指定文本末尾
INSERT：来指定当前插入点。
"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog
from tkinter import StringVar



def load():
    global count_words
    try:
        with open(filename.get()) as file:
            contents.delete('1.0', END) # 在加载新文件前删除文本框中的内容
            contents.insert(INSERT, file.read())
    except:
        file_path = filedialog.askopenfilenames(filetypes=[("text file", "*.txt"),("all","*.*")])
        try:
            with open(file_path[0]) as file:
                contents.delete('1.0', END)
                contents.insert(INSERT, file.read())
        except:pass

    count_words.set('字数：'+str(len(contents.get('1.0', END)) - 1))

def save():
    try:
        with open(filename.get(), 'w') as file:
            file.write(contents.get('1.0', END)) # ？
    except:
        messagebox.showinfo("警告！！！", "您没有输入文件名或者内容")

def reset():
    filename.delete(0, END)



top = Tk() # 创建主窗口
top.config( bg='silver' )
top.title( "Simple Editor" ) # 指定此程序名称
top.geometry("900x700")
top.iconbitmap(r'E:\wcc\图片\字符画\mylog.ico')



contents = ScrolledText( bd =2.5, font='楷体' ) # 文本区域
contents.pack( side=BOTTOM,
               expand=True,
               fill=BOTH )

count_words = StringVar()
count_words.set('0')
Label(contents,
      textvariable=count_words,
      bg='snow'
      ).pack(side=BOTTOM)



Label( text='请输入文件名:',
       font=("楷体",13),
       bg="silver"  #背景颜色
     ).pack(side=LEFT )


filename = Entry( bd =2.5,
                  relief=RIDGE
                  ) # 设置文件名区域
filename.pack( side=LEFT,
               expand=True,
               fill=X )


Button( text='Open',
        command=load,
        activebackground='gray'
        ).pack(side=LEFT )

Button( text='Save',
        command=save,
        activebackground='gray'
        ).pack(side=LEFT )

Button( text='Reset',
        command=reset,
        activebackground='gray'
        ).pack(side=LEFT )


mainloop()