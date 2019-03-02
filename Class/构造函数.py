"""
在Python中，创建构造函数很容易，只需将方法init的名称从普通的init改为
魔法版__init__ 即可。
"""

class Math:
    def __init__(self,value):
        self.integer = value

    def squared(self):
        print(self.integer**2)


class AdvMath(Math):
    def __init__(self,value_2):
        super(AdvMath,self).__init__(value_2)
        self.float = 2.5

    def addf(self):
        print(self.float+2.0)


m = Math(10)
s = AdvMath(30)

print(m.integer)  #构造函数不同于普通方法的地方在于，将在对象创建后自动调用它们
print(m.squared())
print(s.squared())