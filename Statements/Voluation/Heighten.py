x = 2
y = 2
x = x + 1
y += 1
print(x)
print(y)

#增强赋值也可用于其他数据类型（只要使用的双目运算符可用于这些数据类型）
f = 'foo'
f += 'bar'
f *= 2
print(f)