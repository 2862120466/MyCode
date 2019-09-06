def benary_search(array, item):
    min = 0
    max = len(array)-1

    while max>=min:
        mid = (min+max)//2
        if item>array[mid]:
            min = mid+1
        elif item<array[mid]:
            max = mid-1
        else:
            return mid

    return -1


if __name__ == '__main__':
    print(benary_search([5, 4, 6, 8, 9, 7], 8))