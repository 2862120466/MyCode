'''
单例模式的作用：防止客户端创建多个对象，造成内存浪费或多个对象之间的信息不匹配带来误解

单例模式特点：
1）单例类只能有一个实例
2）单例类必须自己创建自己的唯一实例
3）单例类必须给所有其他对象提供这一实例

实现单例模式的集中方法：
一）Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。

二）静态变量方法
先执行了类的__new__方法（当不重写这个方法时，默认调用object.__new__），实例化对象；
然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式。
__new__会在创建对象时被调用。__init__在创建对象后被调用

三）装饰器实现
原理同上，同样是在创建对象是进行一次对实例的判定

'''


'''
利用python模块实现单例
'''

class SingletonModule():
    pass

singleton1 = SingletonModule()
# from 单例模式 import singleton1


'''
利用静态变量方法实现单例
'''
class Singleton(object):
    '''
    单例类
    '''
    def __new__(cls,a):
        '''
        如果已经存在一个实例对象，则返回一开始创建的对象，不会再创建一个新对象
        :param hasattr: hasattr返回对象是否具有具有给定名称的属性。
        :return: 一个实例对象
        '''

        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self,a):
        self.a = a

    def output_name(self):
        print(self.a)


singleton = Singleton("singleton")
singleton_false = Singleton("singleton_false")  # 这里看似创建了两个对象，实际上他们是一个相同的对象


'''
利用装饰器实现单例模式
'''
def singleton_decorator(cls, *args, **kw):
    instance = {}
    def _singleton(args):
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

@singleton_decorator
class A:
    pass

if __name__ == "__main__":
    print(Singleton.__instancecheck__(singleton))  # output：True
    print(Singleton.__instancecheck__(singleton_false))  # output：True

    singleton.output_name()  # output：singleton_false
    singleton_false.output_name() # output：singleton_false