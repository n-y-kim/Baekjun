from sys import stdin

while True:
    try:
       x,y = map(int, stdin.readline().split())
       print(x+y)
    except:  exit()