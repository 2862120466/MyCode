# 修改列表：给元素赋值
print()
x = [1,2,3]
x[1] =  4
print(x[1])

# 删除元素
print()
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]  #从列表中删除元素也很容易，只需使用del语句即可
print(names[:])

#给切片赋值
print()
name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)
name[1:] = list('ython')  #通过使用切片赋值，可将切片替换为长度与其不同的序列。
print(name)

print()
numbers = [1,5]  #使用切片赋值还可在不替换原有元素的情况下插入新元素
numbers[1:1] = [2,3,4]
print(numbers)

