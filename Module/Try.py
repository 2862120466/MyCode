import re
txt = 'www.baidu.com'

pat = 'baidu'
pat_2 = '^baidu'
pat_3 = 'm$'
lines = {'line_1','line_2','line_3'}
lines[0] = re.search(pat,txt)
lines[1] = re.search(pat_2,txt)
lines[2] = re.search(pat_3,txt)

for i in lines:
    if i : print('true')
    else : print('no')





