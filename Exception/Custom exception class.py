"""
就像创建其他类一样，但务必直接或间接地继承Exception（这意 味着从任何内置
异常类派生都可以）。因此，自定义异常类的代码类似于下面这样：
"""
class SomeCustomException(Exception): pass