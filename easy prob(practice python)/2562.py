from sys import stdin
x = []
for _ in range(0,9):
    x.append(int(input()))

print(max(x))
print(x.index(max(x))+1)