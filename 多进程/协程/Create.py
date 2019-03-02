import  time

def fun():  #对i进行+1运算
    x = 0  #x初始值没影响
    while True:
        value = yield x #yield用来暂停进程
        if value is not None:  #value不为空值则执行循环体
            print('接到任务......')
            time.sleep(1)
            x = value + 5
            print('任务完成:',end='')

def run(fun):
    next(fun)
    for i in range(3):  # i = 0,1,2
        num = fun.send(i)  #将值i传给value，num为x的值
        print('当前数字:',num)
    fun.close()


if __name__ == '__main__':
    fun = fun()
    run(fun)