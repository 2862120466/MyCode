def decorator(func):
    def inner(*args,**kwargs):
        print('this is inner')
        ret = func(*args,**kwargs)
        return ret
    return inner

@decorator
def have_return(a):
    return a

@decorator
def no_return(b):
    print(b)

ret1 = have_return(1234)
ret2 = no_return(6789)

print(ret1,ret2)