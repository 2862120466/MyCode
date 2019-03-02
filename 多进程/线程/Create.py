import multiprocessing,threading

#其用法基本与进程用法一致
#但每一个进程
print(multiprocessing.current_process().name)
print(threading.current_thread().name)