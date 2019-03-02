def simple_coroutine():
    print('-> start')
    x = yield
    print('-> recived', x)

sc = simple_coroutine()

next(sc)
sc.send('zhexiao')