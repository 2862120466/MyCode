#方法append用于将一个对象附加到列表末尾。append也就地修改列表。这意味着它不会返回修 改后的新列表，而是直接修改旧列表。这通常正是你想要的，但有时会带来麻烦
lst = [1, 2, 3]
lst.append(4)
print(lst)

#方法clear就地清空列表的内容。
print()
lst2 = [4,5,6]
lst2.clear()
print(lst2)

#方法 copy 复制列表。前面说过，常规复制只是将另一个名称关联到列表。
print()
a = [1, 2, 3]
b = a
b[1] = 4
print(a)

c = [1,2,3]
d = c.copy()
d[1] = 4
print(c)

#方法count计算指定的元素在列表中出现了多少次。
print()
print( ['to', 'be', 'or', 'not', 'to', 'be'].count('to') )

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1),x.count([1,2]))

#方法extend让你能够同时将多个值附加到列表末尾，为此可将这些值组成的序列作为参数提 供给方法extend。换而言之，你可使用一个列表来扩展另一个列表。
print()
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

#方法index在列表中查找指定值第一次出现的索引
print()
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))

#方法insert用于将一个对象插入列表。
print()
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

#方法pop从列表中删除一个元素（末尾为后一个元素），并返回这一元素。
print()
x= [1,2,3]
print(x.pop(),x.pop(1))
print(x)
#pop是唯一既修改列表又返回一个非None值的列表方法。

#方法remove用于删除第一个为指定值的元素。
print()
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print(x)

#方法reverse按相反的顺序排列列表中的元素
print()
y = [1,2,3]
x = 'abc'
print(list(reversed(x)))
y.reverse()
print(y)

#方法sort用于对列表就地排序①。就地排序意味着对原来的列表进行修改，使其元素按顺序排列，而不是返回排序后的列表的副本。
#方法sort接受两个可选参数：key和reverse
print()
z = [4, 6, 2, 1, 7, 9]
q = [4, 6, 2, 1, 7, 9]
z.sort()

w = sorted(q)  #为获取排序_后_的列表的副本， 另一种方式是使用函数sorted
print(z)
print(q,w)

# >>> x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
# >>> x.sort(key=len)
# >>> x
# ['add', 'acme', 'aerate', 'abalone', 'aardvark']

# >>> x = [4, 6, 2, 1, 7, 9]
# >>> x.sort(reverse=True)
# >>> x
# [9, 7, 6, 4, 2, 1]



















