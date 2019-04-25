from multiprocessing import Pool,Process
import time
import os


def copy_file(old_path_name, new_path_name):

    with open(old_path_name, 'rb') as fo:
        content = fo.read()

    with open(new_path_name, 'wb') as fn:
        fn.write(content)



if __name__ == '__main__':
    old_path = r'E:\Study\Python-Pycharm\项目\多任务\进程\old_file'
    new_path = r'E:\Study\Python-Pycharm\项目\多任务\进程\new_file'

    pp = Pool(4)
    file_name_list = os.listdir(old_path) # 获取目录中所有文件的文件名

    start = time.time()
    for file_name in file_name_list:
        old_path_name = os.path.join(old_path, file_name)
        new_path_name = os.path.join(new_path, file_name)
        # 不创建进程，直接copy文件
        # start = time.time()
        # for file_name in file_name_list:
        #     old_path_name = os.path.join(old_path, file_name)
        #     new_path_name = os.path.join(new_path, file_name)
        #     # 每copy一个文件都创建一个进程
        #     copy_file(old_path_name, new_path_name)
        #
        # end = time.time()
        # print(end-start) # out：1.1169748306274414


        # 每copy一个文件都创建一个进程
        # Process(target=copy_file,args=(old_path_name, new_path_name)).start()
        # out：2.4765892028808594 创建进程的过程十分消耗资源

        # 使用进程池，每copy一个文件都创建一个进程
        pp.apply_async(copy_file, (old_path_name, new_path_name))
        # out：0.001003265380859375 使用进程池能减少创建进程的资源消耗

    end = time.time()
    print(end-start)