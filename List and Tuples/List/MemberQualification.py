#成员资格
#要检查特定的值是否包含在序列中，可使用运算符in,它检查是否满足指定的条件，并返回相应的值：满足时返回True， 不满足时返回False
#in只能检查单个字符

permissions = 'rw'
print()
print('w' in permissions)
print('x' in permissions)

print()
users = ['Wcc','Tgw','lenove']
print(input('Enter your user name: ') in users )

