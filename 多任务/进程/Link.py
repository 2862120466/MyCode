import time,multiprocessing

def ocr(link):
    for value in ['one','two','three']:
        print('.....已完成取词————')
        link.put(value)
        time.sleep(1)

def dic(link):
    dict = {'one':'1','two':'2','three':'3'}

    while True:
        value = link.get()
        print(value,':',dict[value],sep='')

if __name__ == '__main__':
    link = multiprocessing.Queue()

    process_1 =multiprocessing.Process(target=ocr,args=(link,))
    process_2 =multiprocessing.Process(target=dic,args=(link,))

    process_1.start()
    process_2.start()
    #因为dic（）函数是个死循环，所有需要结束进程
    process_1.join()  #等待进程1结束
    process_2.terminate()  #要等到进程全部完成工作再结束它