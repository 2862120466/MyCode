from urllib.request import urlopen
import re

webpage = urlopen('http://www.python.org')

#对文本对象进行转码
tern_webpage = webpage.read().decode('utf-8')

#提取所打开网页中链接About的相对URL
n = re.search('<a href="([^"]+)" .*?>about</a>', tern_webpage, re.IGNORECASE)  # re.IGNORECASE的作用是匹配忽略大小写
print(n.group(1))
