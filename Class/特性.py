#特性
class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)
    """
    隐藏存取方法，让所有的属性看起来都 一样。通过存取方法定义的属性通常称
    为特性（property）。
    property()第一个参数是读取参数，第二个参数是写存参数，第三个参数可选，
    为删除属性的方法，第四个参数可选，指定一个字符串
    """


r = Rectangle()
r.width = 100
r.height = 50
r.size = 10,5
print(r.width)
print(r.size)

