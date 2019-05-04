''' 进程不共享内存空间 '''

import time,multiprocessing

def test_1(name):
    # current_process()访问当前进程实例name的特性，
    # 这个特性是当前进程实例的名称
    print(multiprocessing.current_process().name)
    print(name,1)
    time.sleep(0.5)  #进程暂停0.5秒
    print(name,2)
    time.sleep(0.5)
    print(name,3)

def test_2(name):
    print(multiprocessing.current_process().name)
    time.sleep(1)
    print(name,1)
    time.sleep(0.5)
    print(name,2)
    time.sleep(0.5)
    print(name,3)

if __name__ == '__main__':
    print(multiprocessing.current_process().name)

    # 利用Process()方法创建进程变量
    # args用来传递参数
    process_1 = multiprocessing.Process(target=test_1,args=('函数1:',))
    process_2 = multiprocessing.Process(target=test_2,args=('函数2:',))

    # 每次运行的输出次序是不一样的，说明两个进程混合在一起运行，但
    # 因为process_1先启动，所以test_1总是先执行，因为cpu在顺序、
    # 轮流地执行代码，则只有多个cpu才能真正并行执行多个进程
    process_1.start()
    process_2.start()

