class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):  # SPAMFilter是Filter的子类
    def init(self):  # 重写超类Filter的方法init
        self.blocked = ['SPAM']


f = Filter()
f.init()
str1 = [1,2,3]
print(str1)

s = SPAMFilter()
s.init()
str2 = s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])
print(str2)


##########################################################
#要确定一个类是否是另一个类的子类，可使用内置方法issubclass。
print('\n',issubclass(SPAMFilter,Filter))

#如果你有一个类，并想知道它的基类，可访问其特殊属性__bases__。
print('\n',Filter.__bases__)

#确定对象是否是特定类的实例，可使用isinstance
print('\n',isinstance(s,SPAMFilter))
print(isinstance(s,Filter))

#要获悉对象属于哪个类，可使用属性__class__
print('\n',s.__class__)

#要判断对象中是否有特定方法，可使用hasattr
print('\n',hasattr(s,'filter'))

#要判断对象中的方法是否可调用，可以使用callable
print('\n',callable(getattr(s,'filter',None)))  #这里没有在if语句中使用hasattr并直接访问属性，而是使用了getattr（它让我能 够指定属性不存在时使用的默认值，这里为None）








