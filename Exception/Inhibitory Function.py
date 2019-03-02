class MuffledCalculator:
    muffled = False
    def calc(self, expr):  #如果启用了“抑制”功能，方法calc将（隐式地）返回None
        try:
            return eval(expr)  #将字符串str当成有效的表达式来求值并返回计算结果
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

calculator = MuffledCalculator()
"""
将muffied设置位True则开启抑制功能
"""
calculator.muffled = True  # 开启了抑制功能
print( calculator.calc('10 / 0') )

