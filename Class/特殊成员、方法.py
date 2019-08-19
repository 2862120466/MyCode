"""
元素访问：
 __len__(self)：这个方法应返回集合包含的项数，对序列来说为元素个数，对映
  射来说为键值对数。如果__len__返回零（且没有实现覆盖这种行为的__nonzero__），对象在布 尔上下文中将被视为假（就像空的列表、元组、
  字符串和字典一样）。
 __getitem__(self, key)：这个方法应返回与指定键相关联的值。对序列来说，
  键应该是 0~n -1的整数（也可以是负数，这将在后面说明），其中n为序列的长
  度。对映射来说， 键可以是任何类型。
 __setitem__(self, key, value)：这个方法应以与键相关联的方式存储值，以
  便以后能够 使用__getitem__来获取。当然，仅当对象可变时才需要实现这个方法。
 __delitem__(self, key)：这个方法在对对象的组成部分使用__del__语句时被调用，应删除与key相关联的值。同样，
  仅当对象可变（且允许其项被删除）时，才需要实现这个方法。

__doc__ 查看尖的描述信息

__module__表示当前操作的对象所在的模块

__class__表示当前操作的对象所属的类

__init__构造方法 通过类创建对象自动执行

__del__析构方法,当前对象在内存中被释放自动斩妖执行

__call__对象后面加括号触发执行

__dict__查看类或对象中的成员

__str__如果一个类中定义了此方法,那么打印此类对象时,输出此方法的返回值

__getitem__当类中定义了一个字典的属性成员,可以获取

__setitem__设置修改类中字典的数据

__delitem__删除 类中字典的数据

__metalass__其用来表示该类由 谁 来实例化创建

__new__触发 __init__创建实例
"""

class SpecialMethod:
    '''
    测试一些特殊方法
    '''

    def __init__(self, *args, **kwargs):
        '''
        :param args: 收集多个没有key的变量
        :param kwargs: 收集多个有key的变量
        '''
        self.num = args
        self.long = kwargs

    def __len__(self):
        '''
        使得对象能像list一样使用len()函数
        :return: length of self.num
        '''
        return len(self.num)

    def __getitem__(self, index):
        '''
        使得对象能像list一样使用索引取值
        :return: The value of the corresponding index
        '''
        return self.num[index]

    def __setitem__(self, key, value):
        '''
        使得对象能像list一样使用索引赋值
        :param key: index
        :param value: value
        '''
        self.long[key] = value

    def __delitem__(self, key):
        '''
        使得对象能利用del删除指定元素
        :param key: index
        '''
        del self.long[key]

    def __call__(self, arg):
        '''
        使得对象能像函数一样被调用
        :param arg: value
        '''
        self.long['c'] = arg

t = SpecialMethod(1, 2, 3, 4, a=1, b=2, c=3)

print( type(t.num) )  # output: <class 'tuple'>

# __getitem__、__len__
print( t[0] )  # output: 1
print( len(t) )  # output: 4

# __call__、__setitem__、__delitem__
print( t.long )  # output: {'a': 1, 'b': 2, 'c': 3}
t(6)
print( t.long )  # output: {'a': 1, 'b': 2, 'c': 6}
t['d'] = 4
print( t.long )  # output: {'a': 1, 'b': 2, 'c': 6, 'd': 4}
del t['d']
print( t.long )  # output: {'a': 1, 'b': 2, 'c': 6}


print(SpecialMethod.__doc__)