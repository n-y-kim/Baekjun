from sys import stdin

numbers = []

for i in range(46):
    for j in range(i):
        numbers.append(i)

A, B = map(int, stdin.readline().split())
result = 0
for i in range(A-1, B):
    result += numbers[i]

print(result)