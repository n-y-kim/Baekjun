from sys import stdin

t = int(stdin.readline())
result = []

for i in range(t):
    a, b = map(int, stdin.readline().split(','))
    result.append(a+b)

for i in range(t):
    print(result[i])