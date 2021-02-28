from sys import stdin

n,k = map(int,stdin.readline().split())
array = list()
result = list()

for i in range(1,n+1): array.append(i)

num = k-1
result.append(array[num])
del array[num]

while len(result) != n :
    num += k-1
    
    while True:
        if num >= len(array):
            num -= len(array)
        else : break

    result.append(array[num])
    del array[num]
    
print("<",end = '')
for i in range(0,n):
    if i == n-1: print("%d" %(result[i]), end='')
    else: print("%d, "%(result[i]), end= '')
print(">")