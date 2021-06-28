from sys import stdin
from collections import deque

x, y = map(int, stdin.readline().split())
zeroIndex = 1
dates = deque(['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'])

for month in range(1, x):
    if month==2: zeroIndex = 28%7
    elif month ==4 or month==6 or month==9 or month==11: zeroIndex = 30%7
    else: zeroIndex = 31%7
    for i in range(zeroIndex):
        dates.append(dates.popleft())

print(dates[y%7])