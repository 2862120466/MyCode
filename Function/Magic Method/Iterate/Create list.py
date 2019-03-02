"""
使用构造函数list显式地将迭代器转换为列表
"""

class List:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:raise StopIteration
        return self.value
    def __iter__(self):
        return self


lis = List()
print(list(lis))
