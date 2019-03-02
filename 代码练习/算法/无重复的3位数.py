"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
"""
程序分析：
a是百位数；b是十位数；c是个位数
a有4种情况，b有4种情况，c有4种情况
分别将1，2，3，4赋值给他们
z = a*100+b*10+c
去除不符合条件的数
"""
count = 0

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            z = a*100+b*10+c
            if(a!=b!=c and b!=a!=c and c!=a!=b ):
                count +=1
                print(z,end=',')

print('\n',end='')
print('个数为：',count)