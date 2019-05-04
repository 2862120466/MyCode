# def flatten(nested):
#     for sublist in nested:
#         for element in sublist:
#             yield element
#
# nested = [[1, 2], [3, 4], [5]]
# print(list(flatten(nested)))


def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b = b, a + b
        n = n + 1
    return  'done'

g = fib(5)

while True:
    try:
        x = next(g)
        print('generator: ', x)
    except StopIteration as e:
        print("生成器返回值：", e.value)
        break