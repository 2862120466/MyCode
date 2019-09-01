def simple_coroutine():
    y = 0

    while 1:
        x_recv = yield y
        print('-> start')
        y += 10
        print('-> x_recv的值为', x_recv)


sc = simple_coroutine()
x_recv = sc.send(None)
print(x_recv)

for i in range(3):
    y_recv = sc.send('wcc')

    print('当前y_recv的值为%s\n' % y_recv)