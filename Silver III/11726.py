from sys import stdin

n = int(stdin.readline())
numbers = [1]
for i in range(1, n):
    if i==1: numbers.append(numbers[0]+1)
    else: numbers.append(numbers[i-1] + numbers[i-2])

print(numbers[n-1]%10007)