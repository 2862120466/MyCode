"""
函数re.sub从左往右将与模式匹配的子串替换为指定内容。请看下面的示例：
"""
import re
pat = '[A-Z]'
text = 'Hello! nice to meet you! '
line = re.sub(pat,r'[Replace]',text)
print(line)