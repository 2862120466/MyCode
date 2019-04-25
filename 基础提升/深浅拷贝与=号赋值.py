"""
深浅拷贝与=号赋值的测试
对于数字和字符串的赋值、浅拷贝、深拷贝在内存当中用的都是同一块地址

对于列表，字典，元组的赋相同值在内存当中用的都是不同地址
对于列表，字典，元组的变量赋值在内存当中用的都是相同地址

列表，字典，元组的浅拷贝只复制第一层，内嵌列表、字典和元组是复制不到的，复制不到以为着就还要内存的联系

列表，字典，元组的深拷贝全部复制
"""

# a = 2
# b = 2
# print(a is b) out:True

# a = 'czxcasdfafvczxvc'
# b = 'czxcasdfafvczxvc'
# print(a is b)                     out:True

# a = 'abc'
# b = a
# print(a is b)                     out:True


# a = [1,2,3]
# b = [1,2,3]
# print(a is b)                     out : False
# print(a == b)                     out : True

# ls1 = [1,2,3]
# ls2 = ls1
# print(ls1 is ls2)                 out : True
# print(ls1 == ls2)                 out : True
# ls2[2] = 4
# print(ls1)                        out : [1,2,4]

# ls1 = [1,2,3,[6,6,6]]
# ls2 = ls1.copy()
# print( id(ls1), id(ls2) )         out : 51442072 80972336
# print( id(ls1[3]), id(ls2[3]) )   out : 51406408 51406408
# ls2[0] = 0
# print(ls1)                        out : [1, 2, 3, [6, 6, 6]]
# ls2[3] = [9,9,9]
# print(ls1)
#                                   out : [1, 2, 3, [9,9,9]]


import copy
ls1 = [1,2,3,[6,6,6]]
ls2 = copy.deepcopy(ls1)
print( id(ls1), id(ls2) )
print( id(ls1[3]), id(ls2[3]) )
ls2[0] = 0
print(ls1)
ls2[3] = [9,9,9]
print(ls1)