def decorator(func):
    def inner(*args,**kwargs):
        print('The decorator is declared ')
        ret = func(*args,**kwargs)
        return ret
    return inner

@decorator  # output:The decorator is declared
def have_return(a):
    return a

@decorator  # output:The decorator is declared
def no_return(b):
    print(b)

ret1 = have_return('a')
ret2 = no_return('b')  # output:b

print(ret1)  # output:a
print(ret2)  # output:None