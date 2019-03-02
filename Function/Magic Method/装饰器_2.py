def dec1(test):
    print("1111")
    def one():
        print("2222")
        test()
        print("3333")
    return one

def dec2(test):
    print("aaaa")
    def two():
        print("bbbb")
        test()
        print("cccc")
    return two

@dec1
@dec2
def test():
    print("test")

test()

'''
       实质： 是一个函数

　　　　参数：是你要装饰的函数名（并非函数调用）

　　　　返回：是装饰完的函数名（也非函数调用）

　　　　作用：为已经存在的对象添加额外的功能

　　　　特点：不需要对对象做任何的代码上的变动
'''
