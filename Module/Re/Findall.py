"""
找出字符串包含的所有单词
找出所有标点
"""
import re
pat = '[a-zA-Z]+'  #'[a-zA-Z]+'中包含了所有单词的可能
pat_2 = r'[,.!`?/\'"]'
text = r'Hello! nice to meet you! '
print(re.findall(pat,text))
print(re.findall(pat_2,text))
