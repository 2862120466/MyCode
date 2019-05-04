from threading import Thread, Lock

num = 0
lock = Lock()

def run(n):
    global num

    for i in range(1000000):
        lock.acquire() # 上锁
        try:
            num += n
            num -= n
        finally:
            lock.release() # 释放锁

        # with lock:  # 与上面的代码效果相同
        #     num += n
        #     num -= n

if __name__ == '__main__':
    t1 = Thread(target=run, args=(6,))

    t2 = Thread(target=run, args=(9,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(num)