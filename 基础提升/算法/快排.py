def quick(array):
    if len(array)<2:
        return array

    else:
        item = array[0]
        leftelem = [i for i in array[1:]  if i<item ]
        rightelem = [i for i in array[1:]  if i>=item ]
        finallarray = quick(leftelem) + [item] + quick(rightelem)

        return finallarray

if __name__ == '__main__':
    print( quick([5,8,6,3,2,1,5,7]) )