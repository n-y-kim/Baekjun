from sys import stdin

N = stdin.readline()
F = int(stdin.readline())

N_list = list(N)
N_list.pop()

N_front = N_list[:-2]

front_length = len(N_front)
front = 0
for i in range(front_length):
    front += int(N_front.pop()) * 10**i

front *= 100

minNum = 0
for i in range(99):
    temp = front + i
    if temp%F == 0: 
        minNum = i
        break

if minNum<10:
    print(0, end='')
    print(minNum)
else: print(minNum)