#向range传递了第三个参数——步长， 即序列中相邻数的差。通过将步长设置为负数，可让range向下迭代,range(start, stop[, step])
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for number in range(10):
    print(numbers[number])


#迭代字典
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])

for key, value in d.items():
    print(key, 'corresponds to', value)


# 并行迭代
#内置函数zip，它将两个 序列“缝合”起来，并返回一个由元组组成的序列。返回值是一个适合迭代的对象，要查看其内容，可使用list将其转换为列表。
#函数zip可用于“缝合”任意数量的序列。需要指出的是，当序列的长度不同时，函数zip将 在短的序列用完后停止“缝合”。
print()
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')














