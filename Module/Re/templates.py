# templates.py
import fileinput, re

# 与使用方括号括起的字段匹配
field_pat = re.compile(r'\[(.+?)\]')

# 我们将把变量收集到这里：
scope = {}

# 用于调用re.sub：
def replacement(match):
    code = match.group(1)
    try:
        # 如果字段为表达式，就返回其结果：
        return str(eval(code, scope))
    except SyntaxError:
        # 否则在当前作用域内执行该赋值语句
        #  并返回一个空字符串
        return ''

# 获取所有文本并合并成一个字符串：

#（还可采用其他办法来完成这项任务，详情请参见第11章）
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

# 替换所有与字段模式匹配的内容：
print(field_pat.sub(replacement, text))