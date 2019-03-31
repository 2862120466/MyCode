"""
元类是创建类对象的类，所有的类对象的元类都是type类，当然你也可以自己创建元类。

元类的查找机制：
每个类被创建时都会在寻找到自己的元类后再创建，
1.首先会查找自己的类中是否定义有__metaclass__属性，
2.然后再查找父类中是否定义有__metaclass__属性，
3.接着再查找此模块中是否定义有__metaclass__
4.最后再找到type类

在以上4个查找步骤中你可以在前三个步骤中定义元类，来控制自己定义的元类:
__metaclass__ =  XXX

class Test:
    __metaclass__ = XXX
    pass

class Test_2(__metaclass__=XXX):
    pass

"""

class Person:
    name = "wcc"
    sex = "male"

    def run(self):
        print('I am running')

p = Person()

print('对象p的类是：',p.__class__)
print("Person类的元类是：",p.__class__.__class__)
print("int类型的元类是：",int.__class__)
