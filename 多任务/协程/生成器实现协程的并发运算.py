import time
def consumer(name):

    print("%s 准备学习啦!" %name)
    while True:
        lesson = yield
        print("开始[%s]了,[%s]老师来讲课了!" %(lesson,name))
        time.sleep(2) # 实际上并没有并发运算


def producer():
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("同学们开始上课 了!")
    for i in range(5):

        print("\n到了两个同学!")
        c.send(i)
        c2.send(i)

producer()