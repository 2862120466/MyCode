from urllib.request import urlopen
webpage = urlopen(r'file:E:\text.txt')

print(webpage.read().decode('utf-8'))

"""  下面对for循环的练习
text_i = webpage.read().decode('utf-8')  #python3默认字符编码为utf_8模式，而txt文本为byte编码，需要用decode()将其转换
print(type(text_i))

lines = []
for line in text_i:
    lines.append(line)

text_o = ''.join(lines)

print(text_o)
"""
