from sys import stdin
n = int(stdin.readline())
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(n-i):
        print('*', end='')
    print()