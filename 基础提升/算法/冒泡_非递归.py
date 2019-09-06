def bubble_sort3(arr):
    '''
    冒泡排序，第一个值与第二个值比较，小于的话位置不变，大于的话交换位置
    每冒一个泡待排序数组便少一个不用排序的值，这个值会被冒泡到数组最后一位
    所以需要两个for循环，外层循环迭代出待排序数组的元素个数，
    内层循环根据待排序个数进行迭代（有多少个迭代多少次），内部进行比较与换位
    :param arr:
    :return:
    '''
    for i in range(len(arr) - 1, 0, -1):
        count = 0
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        if count == 0:
            return

arr = [5, 2, 7, 3, 9]
bubble_sort3(arr)
print(arr)