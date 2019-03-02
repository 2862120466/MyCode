#步长
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print( numbers[0:10:1] )  #步长为1。这意味着从一个元素移到下一个元素，因此切片包含起点和终点之间的所 有元素。
print( numbers[::2] )  #步长为2时，将从起点和终点之间每隔一个元素提取一个元素。
print( numbers[3:6:3] )
print( numbers[::-1])  #步长不能为0，否则无法向前移动，但可以为负数，即从右向左提取元素。
print( numbers[:3:1] )
print( numbers[-3::1] )
