#Myself.py
def greet():
    print("Hello,world")
def test():
    greet()
if __name__ == '__main__':test()  #?


















"""
要告诉解释器去哪里查找这个模块：
    可执行如下命令（以Windows目录为例）： 
    >>> import sys 
    >>> sys.path.append('C:/python') 
之后便可以导入此模块，模块只能导入一次


将模块放在正确的位置:
    import sys,pprint
    pprint.pprint(sys.path)
目录site-packages是佳的选择，因为它就是用来放置模块的。请 在你的计算机中查看
sys.path，找到目录site-packages，并将模块保存到这里
只要模块位于类似于site-packages这样的地方，所有的程序就都能够导入它。 
"""