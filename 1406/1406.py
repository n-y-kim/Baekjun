from sys import stdin
from collections import deque

arr = deque(stdin.readline())
del arr[len(arr)-1]
m = int(stdin.readline())
cursor = len(arr)

for i in range(0,m):
    command = deque(stdin.readline())
    if command[0] == 'L':
        if cursor == 0: continue
        else: cursor -= 1

    elif command[0] == 'D':
        if cursor == len(arr): continue
        else: cursor += 1

    elif command[0] == 'B':
        if cursor == 0: continue
        else:
            del arr[cursor-1]
            cursor -= 1

    else:
        addLetter = command[2]
        arr.insert(cursor,addLetter)
        cursor += 1

for letter in arr:
    print(letter,end='')
print()