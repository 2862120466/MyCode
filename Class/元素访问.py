"""
元素访问：
 __len__(self)：这个方法应返回集合包含的项数，对序列来说为元素个数，对映
  射来说 为键值对数。如果__len__返回零（且没有实现覆盖这种行为
  的__nonzero__），对象在布 尔上下文中将被视为假（就像空的列表、元组、
  字符串和字典一样）。
 __getitem__(self, key)：这个方法应返回与指定键相关联的值。对序列来说，
  键应该是 0~n -1的整数（也可以是负数，这将在后面说明），其中n为序列的长
  度。对映射来说， 键可以是任何类型。
 __setitem__(self, key, value)：这个方法应以与键相关联的方式存储值，以
  便以后能够 使用__getitem__来获取。当然，仅当对象可变时才需要实现这个方法。
 __delitem__(self, key)：这个方法在对对象的组成部分使用__del__语句时被
  调用，应 删除与key相关联的值。同样，仅当对象可变（且允许其项被删除）时，才
  需要实现这个 方法。
"""



def check_index(key):
    """
    指定的键是否是可接受的索引？
    键必须是非负整数，才是可接受的。如果不是整数，
    将引发TypeError异常；如果是负数，将引发IndexError异常
   （因为这个序列的长度是无穷的）
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError


#给序列计算指定起始位置和步长后的值（计算一次）
class ArithmeticSequence:
   def __init__(self, start=0, step=1):
       """
       初始化这个算术序列
       start   -序列中的第一个值
       step    -两个相邻值的差
       changed -一个字典，包含用户修改后的值
       """
       self.start = start      # 存储起始值
       self.step = step     # 存储步长值
       self.changed = {}    # 没有任何元素被修改

   def __getitem__(self,key):
       """
         从算术序列中获取一个元素
       """
       check_index(key)

       try: return self.changed[key]   # 修改过
       except KeyError:                # 如果没有修改过
            return self.start + key * self.step   # 就计算元素的值

   def __setitem__(self, key, value):
       """
         修改算术序列中的元素
       """
       check_index(key)
       print("seted")

       self.changed[key] = value  # 存储修改后的值



s = ArithmeticSequence(1, 2)
print(s[4])

