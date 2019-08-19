'''
1、2、3、4、5 能组成多少个互不相同且无重复的三位数
'''
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
                if (x!=y) and (y!=z) and (z!=x):
                        print("%d%d%d" % (x, y, z))