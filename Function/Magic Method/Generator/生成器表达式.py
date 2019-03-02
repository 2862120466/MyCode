"""
列表推导式使用的[],而生成器表达式使用的是()
"""

a = (i*i for i in range(10) )
print(type(a))

for lis in a:
    print(lis)