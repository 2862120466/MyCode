'''
探索 i += 1 与 i = i+1 的区别
'''

'''
对于不可变对象int str tuple
都会创建一个新的内存地址
'''
i = 0
print(id(i))  # 1564271360
i += 1
print(id(i))  # 1564271376
i = i + 1
print(id(i))  # 1564271392


'''
对于可变类型对象 i+=1不会改变内存地址, i = i+1会改变内存地址
'''
list = [1,2,3]
print(id(list))  # 78555136
list += [4]
print(id(list))  # 78555136
list = list + [5]
print(id(list))  # 78555497


