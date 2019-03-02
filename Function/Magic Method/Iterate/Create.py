"""
方法__iter__返回一个迭代器，它是包含方法__next__的对象，而调用这个方法时
可不提供 任何参数。当你调用方法__next__时，迭代器应返回其下一个值。如果迭
代器没有可供返回的值， 应引发StopIteration异常。你还可使用内置的便利
函数next，在这种情况下，next(it)与 it.__next__()等效
"""


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b,self.b+self.a
        return self.a
    def __iter__(self):
        return self
"""
而这个方法返回迭代器本身。在很多情况下，都在 另一个对象中实现返回迭代器的方
法__iter__，并在for循环中使用这个对象。但推荐在迭代器 中也实现方法__iter__
（并像刚才那样让它返回self），这样迭代器就可直接用于for循环中。 
"""


fibs = Fibs()

for f in fibs:
    if f > 100:  #找出第一个大于100的斐波那契数
        print(f)
        break