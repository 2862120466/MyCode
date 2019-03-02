#递归式生成器:解决多层嵌套列表
"""
在生成器开头进行检查。要检查对象是否类似于字符串，简单、 快捷的方式是，尝
试将对象与一个字符串拼接起来，并检查这是否会引发TypeError异常
"""
def flatten(nested):
    try:
        # 不迭代类似于字符串的对象：
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

print( list(flatten(['foo', ['bar', ['baz']]])) )