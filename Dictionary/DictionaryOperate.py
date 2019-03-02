#字典的基本行为在很多方面都类似于序列。
#  len(d)返回字典d包含的项（键值对）数。
#  d[k]返回与键k相关联的值。
#  d[k] = v将值v关联到键k。
#  del d[k]删除键为k的项。
#  k in d检查字典d是否包含键为k的项。

#赋值
x = {'Tgw':'11'}
x['42'] = 'wcc'
print(x['42'])

#将字符串格式设置功能用于字典
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print("Cecil's phone number is {Cecil}.".format_map(phonebook))


