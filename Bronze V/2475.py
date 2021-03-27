from sys import stdin
num = list(map(int,stdin.readline().split()))
sumNum = 0
for n in num:
    sumNum += n**2
print(int(sumNum%10))