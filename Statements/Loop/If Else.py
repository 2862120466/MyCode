num = int(input('Enter a number: '))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')

#让程序在错误条件出现时立即崩溃
#你可要求某些条件得到满足（如核实函数参数满足要求或为初始测试和调试提 供帮助），为此可在语句中使用关键字assert。
"""
>>> age = 10
>>> assert 0 < age < 100
>>> age = -1
>>> assert 0 < age < 100
Traceback (most recent call last):
File "<stdin>", line 1, in ?
AssertionError

"""