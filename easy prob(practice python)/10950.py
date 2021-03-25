from sys import stdin
n = int(stdin.readline())
for i in range(0,n): 
    a,b = map(int, stdin.readline().split())
    print(a+b)