from sys import stdin
x = []
count = [0,0,0,0,0,0,0,0,0,0]
for _ in range(3):
    y = int(stdin.readline())
    x.append(y)

num = str(x[0] * x[1] * x[2])
for i in range(0,10):
    print(num.count(str(i)))