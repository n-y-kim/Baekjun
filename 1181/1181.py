from sys import stdin
from collections import deque

N = int(stdin.readline())
wordArr = []
for i in range(N):
    arr = list(stdin.readline())
    arr.pop()
    wordArr.append(arr)

result = deque()
shortest = 50

for arr in wordArr:
    if len(arr) < shortest:
        result.appendleft(str(arr))
        shortest = len(arr)
    elif len(arr) == shortest:

    elif len(arr) > shortest:
        result.append(str(arr))
        

    