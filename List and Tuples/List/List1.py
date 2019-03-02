edward =['Edward Gumby', 42]
wcc =['Wcc Smith', 50]
datebase = [edward,wcc]
print(datebase)


#引索
getting='Hello'
print(getting[0]+"(1)")           #取第一个字符
print(getting[-1]+"(2)")          #取最后一个字符
print('Test'[0]+"(3)")            #对于字符串字面量（以及其他的序列字面量），可直接对其执行索引操作，无需先将其赋给 变量

fourth = input('Please input Year: '+"(4)")[3]
print(fourth)             #如果函数调用返回一个序列，可直接对其执行索引操作


#切片                              #，切片适用于提取序列的一部分，其中的编号非常重要：第一个索引是包含的第一 个元素的编号，但第二个索引是切片后余下的第一个元素的编号
tag = '<a href="http://www.python.org">Python web site</a>'
print()
print(tag[9:30] +"(5)")
print( tag[32:-4] +"(6)")
#简写
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print()
print( numbers[-3:-1])
print( numbers[-3:])
print( numbers[3:10])
print( numbers[:3])
print( numbers[:])



#长度、最小值和最大值
print()
print( len(numbers) )
print( max(numbers) )
print( min(numbers) )
print( max(2,3) )
print( min(2,3) )

# 修改列表：给元素赋值
print()
x = [1,2,3]
x[1] =  4
print(x[1])