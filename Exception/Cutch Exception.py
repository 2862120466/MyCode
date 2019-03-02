#使用except Exception as e: 对异常对象进行检查
#加入while True循环：只要出现错误，程序就会要求用户提供新的输入

try:
    x = int(input("please enter your first number:"))
    y = int(input("please enter your second number:"))
    print(x/y)
except ZeroDivisionError:  #捕获ZeroDivisionError类型的异常
    print('\n',"Error:The second number can't be zero")
except (ValueError,TypeError):  #捕获多个异常，在一个元祖中指定这些异常
    print("The value is wrong")
else:  #程序没有错误将执行else代码块
    print("No wrong")
finally:
    print('over')


"""
引发别的异常:
你可使用raise ... from ...语句来提供自己的异常上下文，也可使用None
   来禁用上下文。 
try:
    1/0
except ZeroDivisionError:
    raise ValueError from None

异常显示:
Traceback (most recent call last):   
    File "<stdin>", line 2, in <module> 
ZeroDivisionError: division by zero 

在处理上述异常时，引发了另一个异常： 
Traceback (most recent call last):   
    File "<stdin>", line 4, in <module> 
ValueError
"""