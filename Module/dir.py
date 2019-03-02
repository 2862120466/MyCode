import sys  #让解释器能找到模块
sys.path.append('E:\Study\Python-Pycharm\Module')

import Myself
print( [n for n in dir(Myself) if not n.startswith('__')] )
"""
列出对象的所有属性（对于模块，它列出所有的函数、类、变量等）。如果将dir(Myself)的结
果打印出来，将是一个很长的名称列表（请试试 看）。在这些名称中，有几个以下划线打头。
根据约定，这意味着它们并非供外部使用。有鉴于此，我们使用一个简单的列表推导将这些名
称过滤掉
"""