from sys import stdin
from collections import deque

def reverse(li):
    result = 0
    for i in range(3):
        result += int(li.popleft()) * 10 ** i
    return result

A, B = stdin.readline().split()

A_list = deque(A)
B_list = deque(B)

print(A_list)

A_reversed = reverse(A_list)
B_reversed = reverse(B_list)

if A_reversed > B_reversed: print(A_reversed)
else: print(B_reversed)