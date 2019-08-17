"""
求一组数的平均值
"""
def get_avg(*a):
    sum = 0
    for i in a:
        sum += i
    return sum / len(a)

if __name__=="__main__":
    print(get_avg(1,2,3,3))

