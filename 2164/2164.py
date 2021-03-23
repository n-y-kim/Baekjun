from sys import stdin
from collections import deque
#list
def delete():
    d.pop()

def deleteAndAdd(num):
    d.pop()
    d.insert(0,num)


N = int(stdin.readline())
d = deque()

for i in range(1,N+1):
    d.append(i)
d.reverse()

while len(d) != 0:
    if len(d) == 1: 
        print(d[0])
        exit()
    try:
        delete()
        deleteAndAdd(d[-1])
    except: 
        delete()
    