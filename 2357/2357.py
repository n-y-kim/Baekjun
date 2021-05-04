from sys import stdin
from collections import deque 

def findMin(N_sliced):
    minimum = 1000000000
    for num in N_sliced:
        if num < minimum : minimum = num

    return minimum

def findMax(N_sliced):
    maximum = 1
    for num in N_sliced:
        if num > maximum : maximum = num

    return maximum


N, M = map(int, stdin.readline().split())
N_input = deque();

for i in range(N):
    N_input.append(int(stdin.readline()))

M_input = deque();
for i in range(M):
    m_input = deque(map(int, stdin.readline().split()))
    M_input.append(m_input)

for i in range(M):
    N_sliced = deque();
    for j in range(M_input[i][0]-1, M_input[i][1]):
        N_sliced.append(N_input[j]);
    minimum = findMin(N_sliced)
    maximum = findMax(N_sliced)

    print("%d %d" %(minimum, maximum))