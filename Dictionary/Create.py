#字典的创建
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
#可使用函数dict①从其他映射（如其他字典）或键值对序列创建字典。
items = [('name','Gtmby'),('age',42)]
d = dict(items)
print(d)
print(d['name'])  #字典的查询


#还可使用关键字实参来调用这个函数，如下所示：
# >>> d = dict(name='Gumby', age=042)
# >>> d
# {'age': 42, 'name': 'Gumby'} 