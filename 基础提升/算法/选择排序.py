def selection_sort(arr):
    '''
    选择排序算法，找到数组中最小的元素。和数组第一个元素交换位置
    再去剩下元素继续比较
    时间效率取决于比较次数
    运行时间与输入无关，数据移动最少
    :param arr:0
    :return:
    '''
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == '__main__':
    print(selection_sort([4, 2, 5, 2, 3, 7]))