class TestPropety:
    def __init__(self):
        self.width = 0
        self.height = 0
    def getsize(self):
        return self.width,self.height

    def setsize(self,size):
        self.width,self.height = size

    size = property(getsize,setsize)

t = TestPropety()

t.size = 5,10

print(t.width,t.height)