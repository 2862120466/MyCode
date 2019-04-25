"""
实例方法：第一个参数传递的是实例(self)，此方法对实例进行操作
静态方法：，需要传递@classmethod装饰器，且第一个参数传递的是类(cls)，此方法对类进行操作，各实例的操作不会影响这个方法
类方法：需要传递@staticmethod装饰器，不传递默认参数
"""

class Person:
    name = 'wcc' #这是一个类属性
    def instanceFunc(self):
        print('this is a instance function',self.name)

    @classmethod
    def classFunc(cls):
        print('this is a class function',cls.name)

    @staticmethod
    def staicFunc():
        print('this is a static function',Person.name)


print('\n',"_"*5,'用实例来调用这些方法',"_"*5)

p = Person()
p.instanceFunc()
p.classFunc()
p.staicFunc()

print('\n',"_"*5,'用类来调用这些方法',"-"*5)

Person.classFunc()
Person.staicFunc()
# Person.instanceFunc()  out:error

print('\n',"_"*5,'对类属性的修改影响',"-"*5)
p.name = 'tgw'
p.instanceFunc()
p.classFunc() #实例对类属性的修改并不会影响到通过cls.调用的类属性值
p.staicFunc() #同上