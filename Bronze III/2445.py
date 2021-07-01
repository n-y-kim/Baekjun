from sys import stdin

n = int(stdin.readline())
for i in range(1, n):
    for j in range(i):
        print("*", end='')
    for j in range(2*n-2*i):
        print(" ", end='')
    for j in range(i):
        print("*", end='')
    print()
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end='')
    for j in range(2*n-2*i):
        print(" ", end='')
    for j in range(i):
        print("*", end='')
    print()
