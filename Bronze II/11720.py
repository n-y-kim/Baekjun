from sys import stdin

n = int(stdin.readline())
num = stdin.readline()
result = 0
for i in range(n):
    result += int(num[i])
print(result)