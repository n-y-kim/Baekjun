from sys import stdin
num = []
for i in range(10):
    x = (int(stdin.readline()))
    num.append(x)
result = []
for i in range(0, 10):
    result.append(num[i]%42)
different = 10
result.sort()
for i in range(0,10):
    if i != 9 and result[i] == result[i+1]:
        different -= 1

print(different)