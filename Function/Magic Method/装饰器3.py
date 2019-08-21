'''
func是我要装饰的函数，我想用装饰器显示func函数运行的时间。
@decorator这个语法相当于 执行 func = decorator(func)，为func函数装饰并返回。
在来看一下我们的装饰器函数 - decorator，该函数的传入参数是func （被装饰函数），
返回参数是内层函数。这里的内层函数-wrapper，其实就相当于闭包函数，
它起到装饰给定函数的作用，wrapper参数为*args, **kwargs。*args表示的
参数以列表的形式传入；**kwargs表示的参数以字典的形式传入：
'''

import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print(end_time - start_time)

    return wrapper

@decorator
def func(t):
    time.sleep(t)

func(0.8) # 函数调用
# 输出：0.800644397735595