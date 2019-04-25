"""
这是一个对类中变量的生命周期的测试
类变量objectCoounts计算实例个数，每新增一个实例objectCounts就 +1 ，每del 一个实例objectCounts就 -1
类方法outCounts()输出实例个数
"""

class Person:
    objectCounts = 0
    def __init__(self):
        Person.objectCounts += 1
        print('增加了一个实例')

    def __del__(self):
        print('减少了一个实例')
        Person.objectCounts -= 1

    @classmethod
    def outCounts(cls):
        print(cls.objectCounts)


p = Person()
p2 = Person()

Person.outCounts()

