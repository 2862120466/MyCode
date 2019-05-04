import  time

def func():  #对run中的i进行+5运算
    x = 0  #x初始值没影响
    while True:
        value = yield x #yield用来暂停进程
        if value is not None:  #value不为空值则执行循环体
            print('接到任务......')
            time.sleep(1)
            x = value + 5
            print('任务完成')

def run(func):
    func.send(None) # 相当于 next(func) 都是启动一个生成器

    for i in range(3):  # i = 0,1,2
        print('发送数据 %d 给fun()' % i)
        num = func.send(i)  #将值i传给value，num为x的值
        print('当前数字:%d\n' % num)

    # func.close()


if __name__ == '__main__':
    fun = func()
    run(fun)