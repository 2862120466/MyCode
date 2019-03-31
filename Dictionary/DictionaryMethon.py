#方法clear删除所有的字典项，这种操作是就地执行的（就像list.sort一样），因此什么都不 返回（或者说返回None）
d = {}
d['wcc'] = 'suai'
print(d)
d.clear()
print(d)

#方法copy返回一个新字典，其包含的键值对与原来的字典相同（这个方法执行的是浅复制， 因为值本身是原件，而非副本）。
#这个方法执行的是浅复制， 因为值本身是原件，而非副本
#一种办法是执行深复制，即同时复制值及其包含的所有值，等等。为此， 可使用模块copy中的函数deepcopy。
print()
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

#方法fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None
#如果你不想使用默认值None，可提供特定的值。
print()
print( {}.fromkeys(['name', 'age']) )
print( dict.fromkeys(['name', 'age'], '(unknown)') )

#方法get为访问字典项提供了宽松的环境。通常，如果你试图访问字典中没有的项，将引发 错误。
print()
d = {}
c = {'name':'wcc'}
print(d.get('name'))
print(d.get('name', 'N/A') )  #你可指定“默认” 值，这样将返回你指定的值而不是None
print(c.get('name', 'N/A') )

#方法items返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式。字典项 在列表中的排列顺序不确定。
print()
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())
it = d.items()
d['spam'] = 1
print(('spam',1) in it)  #，它们始终是底层字典的反映，即便你修改了底层字典亦如此

#方法popitem类似于list.pop，但list.pop弹出列表中的后一个元素，而popitem随机地弹出一个字典项，因为字典项的顺序是不确定的，
# 没有“后一个元素”的概念。如果你要以高效 地方式逐个删除并处理所有字典项，这可能很有用，因为这样无需先获取键列表。
print()
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print(d.popitem())
print(d)

#方法setdefault有点像get，因为它也获取与指定键相关联的值，但除此之外，setdefault 还在字典不包含指定的键时，在字典中添加指定的键值对。
print('setdefault')
d = {}
d.setdefault('name','N/A')
print(d.setdefault('name','N/A'))
print(d)

#方法update使用一个字典中的项来更新另一个字典。
#对于通过参数提供的字典，将其项添加到当前字典中。如果当前字典包含键相同的项，就替 换它。
print()
d = {'title': 'Python Web Site',
     'url': 'http://www.python.org',
     'changed': 'Mar 14 22:09:15 MET 2016'}
x =  {'title': 'Python Language Website'}
d.update(x)
print(d)

#方法values返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的视 图可能包含重复的值。
print()
d = {'title': '1',
     'url': '2',
     'changed': '3'}
print(d.values())





















