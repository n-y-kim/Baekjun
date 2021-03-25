from sys import stdin
t = int(stdin.readline())
for i in range(0,t):
    x, y = map(int, stdin.readline().split())
    print(x+y)