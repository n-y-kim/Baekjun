from sys import stdin
from collections import deque
#3가지 연산, 1번: 왼쪽 첫번쨰 원소 pop. 2번 왼쪽 pop하고 끝에 append. 
# 3번.마지막 pop하고 왼쪽 첫번째 원소로 insert.

def firstFunc():
    q.popleft()
    print(q)

def secondFunc(second):
    q.append(q.popleft())
    print(q)
    return second + 1

def thirdFunc(third):
    q.appendleft(q.pop())
    print(q)
    return third + 1


q = deque()
# wantToPop = {}
N, M = map(int, stdin.readline().split())
wantToPop=list(map(int, stdin.readline().split()))
originalWantToPop = list(map(int, stdin.readline().split()))
for i in range(1,N+1): q.append(i)
# for i in range(M):
#     wantToPop[originalWantToPop[i]] = originalWantToPop[i]

second = 0
third = 0

for number in wantToPop:
    while number != q[0]:
        if q.index(number) <= len(q)//2:
            second = secondFunc(second)
            print("second = %d" %second)
        elif q.index(number) > len(q)//2:
            third = thirdFunc(third)
            print("third = %d" %third)
    if number == q[0]: firstFunc()

print(second + third)