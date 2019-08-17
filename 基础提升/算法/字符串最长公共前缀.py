'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
'''
strs = ['flower','flighty','flow']

if len(strs) == 0:
    print('')

res = []

for i in range(len(strs[0])):
    ch = strs[0][i] # f l o w e r
    flg = False
    for s in strs:
        try:
            if s[i] != ch:
                flg = True
                break
        except:
            flg = True
            break

    if flg is False:
        res.append(ch)
    else:
        break

print(''.join(res))