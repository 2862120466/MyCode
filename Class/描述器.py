"""
实现对类属性的控制：检查，计算等
资源描述器：含有方法__get__和__set__的描述器
非资源描述器：只含有__get__方法的描述器
getAttribute优先级：资源描述器 > 实例属性 > 非资源描述器
"""

class Age:
    """
    age描述器，含有方法__get__，__set__，__delete__

    __get__:返回检测、修改后的age值（value）
    __set__:对age值进行检测、修改
    __delete__:删除这个属性
    """
    def __get__(self, instance, owner):
        print('get second execute',owner)

        if instance.value:
            return instance.value
        else:
            return 'aged的值不规范'

    def __set__(self, instance, value):
        print('set first execute')
        """
        instance代表Person类的实例
        value是传递过来的age值
        """
        if value < 0 :
            instance.value = None
        else:
            instance.value = value #将值得存储绑定在Person实例中，否则所有Person实例都会共享一个age

    def __delete__(self, instance):
        pass
        # del instance.value   还不知道怎么让__delete__执行起来


class Person:
    age = Age()


p1 = Person()
p1.age = -1
print(p1.age)

# p2 = Person()
# # p2.age = 12
# # print(p2.age)  out: 12