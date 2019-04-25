"""
实现表达式的计算,实现eval()的功能

属性：
__value_filter          将表达式转换后的计算列表
median                  计算表达式时要用到的中间值
operational_character   一个运算符的元组
self.length             __value_filter的长度

filter()判断条件:
int(self.__value[i-1]).__class__判断它前一个字符是不是符号



"""

import win32com.client


class Calculator:
    __value = []
    __value_filter = []
    median = 0
    __speak_str = ''
    operational_character = ('+', '-', ' *', '/')

    def __init__(self, expression):
        self.__expression = expression

    def __call__(self):
        self.filter()
        self.set_float()
        self.judger()
        self.speak()

    def add(self, a, b):
        sum = a+b
        return sum, sum

    def sub(self, a, b):
        sum = a - b
        return sum, sum

    def mul(self, a, b):
        sum = a * b
        return sum, sum

    def div(self, a, b):
        sum = a / b
        return sum, sum

    def filter(self):
        str = ""

        for i in self.__expression:
            self.__value.append(i)

        for i in range(len(self.__value)):
            try:
                # 如果判定不合格说明这个字符是：  一个符号、一个连续数的开头、单数
                if int(self.__value[i]).__class__ and int(self.__value[i-1]).__class__ :  #这 个字符是整数，它上一个字符也是整数
                    str = str + self.__value[i]
                    try:
                        int(self.__value[i+1])  # 当这个数的下一个字符不是符号时，连续数继续判断
                        pass
                    except:
                        if str[1] == 0:
                            self.__value_filter.append(int(str))  # 当这个数的下一个字符是符号时，连续数存储进列表
                        else:
                            self.__value_filter.append(str)
                        str = ""
            except:
                try:
                    # 如果这个字符是一个连续数的开头，就把他暂存起来
                    if int(self.__value[i]).__class__ and int(self.__value[i+1]).__class__:  # 这个字符是非0整数，它下一个字符是整数
                        str = self.__value[i]  # 暂存连续数的第一个数

                except:
                    try:
                        int(self.__value[i])  # 这个字符是整数
                        self.__value_filter.append(int(self.__value[i]))  # 单数
                    except:
                        self.__value_filter.append(self.__value[i])  # 符号

        print('过滤表达式之后:',self.__value_filter)



    def set_float(self):
        self.length = len(self.__value_filter)
        try:
            for i in range(self.length):
                if self.__value_filter[i] == '.':
                    set = str(self.__value_filter[i-1]) + '.' + str(self.__value_filter[i+1])

                    self.__value_filter[i] = float(set)
                    del self.__value_filter[i+1]
                    del self.__value_filter[i-1]
        except:
            pass
        # 对残余的包含0的整数字符进行取整
        for j in range(len(self.__value_filter)):
            try:
                if self.__value_filter[j].__class__ == str:
                    self.__value_filter[j] = int(self.__value_filter[j])
            except:pass

        self.__speak_str = self.__value_filter.copy()  # 用浅拷贝复制，以免被__value_filter后面的改动影响
        print('设置了浮点数后：',self.__value_filter)


    def judger(self):

        for i in range(len(self.__value_filter)):

            switcher = {
                '+':lambda x:self.add(self.__value_filter[x - 1],self.__value_filter[x + 1]),
                '-':lambda x:self.sub(self.__value_filter[x - 1],self.__value_filter[x + 1]),
                '*':lambda x:self.mul(self.__value_filter[x - 1],self.__value_filter[x + 1]),
                '/':lambda x:self.div(self.__value_filter[x - 1],self.__value_filter[x + 1])
            }
            # 当检测到运算符时执行运算
            if self.__value_filter[i] in self.operational_character:
                self.median, self.__value_filter[i + 1] = switcher.get(self.__value_filter[i])(i)

        print('计算结果是：',self.median)


    def speak(self):
        speaker = win32com.client.Dispatch('SAPI.SpVoice')
        voice_dict = {
            '+':'加',
            '-':'减',
            '*':'乘以',
            '/':'除以'
        }
        for i in self.__speak_str:
            if i.__class__ != str:
                speaker.Speak(i)
            else:
                speaker.Speak(voice_dict.get(i))

        speaker.Speak('=')
        speaker.Speak(self.median)


if __name__ == "__main__":
    expression = input("请输入你的计算序列：")

    c = Calculator(expression)
    c()