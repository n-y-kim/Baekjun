# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다

from queue import Queue
from sys import stdin

def push(num) :
    que.put(num)

def pop():
    if que.qsize() == 0 :
        print(-1)
    else : print(que.get())

def size():
    print(que.qsize())

def empty():
    if que.qsize() == 0: print(1)
    else: print(0)

def front():
    if que.qsize() == 0: print(-1)
    else: print(que.queue[0])

def back():
    if que.qsize() == 0: print(-1)
    else: print(que.queue[que.qsize()-1])


functions = {'pop': pop, 'size': size, 'empty': empty, 'front': front, 'back': back}

inputNum = int(input())
que = Queue()

while inputNum > 0 :
    inputFunc = list(stdin.readline().split())
    if inputFunc[0] == 'push' : push(int(inputFunc[1]))
    else : 
        func = functions[inputFunc[0]]
        func()
    inputNum-=1
