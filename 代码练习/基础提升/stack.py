'''
代码实现堆栈
'''

stack = []

def push(queue):
    '''
    :param queue: 一个有序队列
    :return: None
    '''
    for elem in queue:
        stack.append(elem)

def pop():
    for i in range( len(stack) ):
        print(stack.pop(-1))


if __name__ == '__main__':
    queue = [1,2,3,4,5]
    push(queue)
    pop()