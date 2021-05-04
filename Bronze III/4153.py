from sys import stdin

while(True):
    a, b, c = map(int, stdin.readline().split())
    num = []
    num.append(a)
    num.append(b)
    num.append(c)
    if a==0 and b == 0 and c == 0: exit(0)
    num.sort()
    if num[0] + num[1] > num[2] and num[0]**2 + num[1]**2 == num[2]**2: 
        print("right")
    else: print("wrong")

