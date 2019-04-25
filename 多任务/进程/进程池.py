from multiprocessing import Pool
from time import sleep, time
import random

def run(process_id):
    print('进程%d开始'%process_id)
    start = time()
    sleep(random.choice([1,2,3]))
    end = time()
    print( '进程%d结束，使用时间%0.2f' % (process_id, end-start) )

if __name__ == '__main__':

    print('主进程开始\n')

    pp = Pool(2) # 设置进程池的进程同时运行的个数，默认是计算机cpu的个数

    for i in range(5):
        pp.apply_async(run, (i,)) # 进程池的进程不用启动，直接开始
                                  # 第一个参数是函数名，第二个参数是函数的参数
    pp.close()
    pp.join()

    print('\n主进程结束')