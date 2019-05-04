from threading import Thread
from time import sleep

def run():
    while 1:
        sleep(2)
        print('iiiii')

if __name__ == '__main__':
    t = Thread(target=run)
    t.start()

    while 1:
        sleep(2)
        print('oooo')



