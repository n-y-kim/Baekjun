from sys import stdin
n = int(stdin.readline())
array = list()
for _ in range(n):
    new = int(stdin.readline())
    if new == 0 : 
        array.pop(-1)
    else:
        array.append(new)

result = 0

if len(array) == 0 : 
    print(result)
    exit()

while len(array) != 0:
    result += array.pop(-1)

print(result)