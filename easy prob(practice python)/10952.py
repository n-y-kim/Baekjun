from sys import stdin
while True: 
    x, y = map(int, stdin.readline().split())
    if x==0 and y==0: exit()
    else: print(x+y)