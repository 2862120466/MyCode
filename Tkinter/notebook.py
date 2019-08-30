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

class NoteBook():


    def __init__(self):
        self._top = Tk()  # 创建主窗口
        self._filename = StringVar()
        self._filename.set('')
        self._filepath = Entry(bd=2.5,
                          relief=RIDGE,
                          textvariable=self._filename
                          )  # 设置文件名区域
        self._contents = ScrolledText(bd=2.5, font='楷体')  # 文本区域
        self._lines = StringVar()
        self._lines.set('0')

    def load(self):
        try:
            with open(self._filepath.get()) as file:
                self._contents.delete(0, END) # 在加载新文件前删除文本框中的内容
                self._contents.insert(0, file.read())
        except:
            if messagebox.askokcancel("提示", "您没有输入文件名或者输入文件名错误，\n是否为你打开选择文件的窗口?") == True:
                initpath = 'C:\\Users\\Administrator\\Desktop'
                file_path = filedialog.askopenfilenames(filetypes=[("text file", "*.txt"),("all","*.*")],
                                                        initialdir=initpath)
                try:
                    with open(file_path[0]) as file:
                        self._filename.set(file_path[0])
                        self._contents.delete('1.0', END)
                        self._contents.insert(INSERT, file.read())
                except:pass
        self.count_lines()  # 在打开文件后启用行数计数器

    def save(self):
        try:
            with open(self._filepath.get(), 'w') as file:
                file.write(self._contents.get('1.0', END)) # ？
        except:
            messagebox.showinfo("警告！！！", "您没有输入文件名或者内容")

    def reset(self):
        self._filepath.delete(0, END)

    def clear(self):
        self._contents.delete('1.0', END)

    def count_lines(self):
        self._lines.set(str(len(self._contents.get('1.0', END).strip().split('\n'))-1) + '行')
        self._top.after(2000, self.count_lines)  # after方法会在程序执行后在指定时间内调用一次，在此函数内部使用此方法达到循环、监听的目的

    def window(self):
        self._top.config(bg='silver')
        self._top.title("Simple Editor") # 指定此程序名称
        self._top.geometry("900x700")
        self._top.iconbitmap(r'E:\wcc\图片\字符画\mylog.ico')

        self._contents.pack(side=BOTTOM,
                           expand=True,
                           fill=BOTH)

        Label(self._contents,
              textvariable=self._lines,
              bg='snow'
              ).pack(side=BOTTOM)


        Label( text='请输入文件路径:',
               font=("楷体",13),
               bg="silver"  #背景颜色
               ).pack(side=LEFT )

        self._filepath.pack(side=LEFT,
                           expand=True,
                           fill=X)


        Button(text='Open',
               command=self.load,
               activebackground='gray'
               ).pack(side=LEFT)

        Button(text='Save',
               command=self.save,
               activebackground='gray'
               ).pack(side=LEFT)

        Button(text='ResetPath',
               command=self.reset,
               activebackground='gray'
               ).pack(side=LEFT)
        Button(text='clear',
               command=self.clear,
               activebackground='gray'
               ).pack(side=LEFT)


        self._top.mainloop()


if __name__ == '__main__':
    NoteBook().window()