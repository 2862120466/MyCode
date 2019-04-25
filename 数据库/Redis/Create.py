import redis

class String():
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0, password=682240)

    def set(self):
        rest = self.r.set('user2', 'Amy')
        return rest

    def get(self):
        rest = self.r.get('user2')
        print(rest)
        return rest

    def mset(self):
        d = {
            'user3': 'Bob',
            'user4': 'Jim'
        }
        rest = self.r.mset(d)
        print(rest)
        return rest

    def mget(self):
        rest = self.r.mget('user3','user4')
        print(rest)
        return rest

class List():
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0, password=682240)

    def lpush(self):
        rest = self.r.lpush('l_eat','Amy','Jhon','wcc')
        print(rest)
        return rest

    def lrange(self):
        rest = self.r.lrange('l_eat',0,-1)
        print(rest)
        return rest

    def lpop(self):
        rest = self.r.lpop('l_eat')
        data = self.r.lrange('l_eat',0,-1)
        print('删除的是：',rest,' 剩下的元素有：',data)
        return rest

class Set():
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0, password=682240)

    def sadd(self):
        rest = self.r.sadd('python_set_roommate','吴长城', '冉杰', '李玉海', '胡佳太')
        print(rest)
        return rest

    def smembers(self):
        rest  = self.r.smembers('python_set_roommate')
        print(rest)
        return rest

    def scary(self):
        rest = self.r.scard('python_set_roommate')
        print(rest)
        return rest


def main():
    # str_obj = String()
    # str_obj.set()
    # str_obj.get()
    # str_obj.mset()
    # str_obj.mget()

    list_obj = List()
    # list_obj.lpush()
    # list_obj.lrange()
    list_obj.lpop()

if __name__ == '__main__':
    main()