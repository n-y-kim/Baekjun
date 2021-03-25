from sys import stdin
t = int(stdin.readline())
for i in range(1,t+1) :
    a, b = map(int, stdin.readline().split())
    print("Case #%d: %d + %d = %d" %(i,a,b,a+b))