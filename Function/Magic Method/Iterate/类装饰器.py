class check:
    def __init__(self,func):
        self.f = func

    def __call__(self, *args, **kwargs):
        print('验证一下')
        self.f()

@check
def fass():
    print('发说说')

# fass = check(fass)

fass()