from sys import stdin
n, x = map(int, stdin.readline().split())
array = list(map(int,stdin.readline().split()))
for arr in array : 
    if arr < x : print("%d " %(arr), end = '')
print()