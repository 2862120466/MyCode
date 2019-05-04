"""
使用封装的进程类时，在启动子进程时，会自动调用类中定义的方法
"""

from multiprocessing import Process

class WccProcess(Process):

    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print('子进程在运行了---%s' % self.name)


if __name__ == '__main__':
    p = WccProcess('process_1')

    p.start() # 在启动子进程时，会自动调用封装进程类中的方法
    p.join()