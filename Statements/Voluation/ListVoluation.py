# 序列解包
values = 1, 2, 3
x,y,z = values
print(x,y,z)

x,y = y,x  #交换多个变量的值。
print(x,y,z)

#可使用星号运算符（*）来收集多余的值，这样无需确保值和变量的个数相同，如下例所示：
#可将带星号的变量放在任意位置。
print()
a,*b,c = 1,2,3,4
print(b)