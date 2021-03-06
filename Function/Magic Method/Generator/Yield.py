def fab(max):
    n, a, b = 0, 0, 1
    for i in range(max):
        yield b  # 把 print b 改为了 yield b，就在保持简洁性的同时获得了 iterable 的效果。
        # print(b)
        a, b = b, a + b
        n = n + 1


# f = fab(5)
# print(list(f))

f = fab(5)  #可以手动调用 fab(5) 的 next() 方法
# next()的返回值是yield表达式后面的值,也就是生成器下一个返回值
print('获取首个返回值:%d' % next(f))
print(list(f))



"""
yield能让进程暂停,通过next()将其激活
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一
个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行
fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执
行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下
次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上
0次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
"""