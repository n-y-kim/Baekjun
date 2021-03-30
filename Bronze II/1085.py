from sys import stdin

x, y, w, h = map(int,stdin.readline().split())
cases = [h-y, y, x, w-x]
cases.sort()
print(cases[0])
