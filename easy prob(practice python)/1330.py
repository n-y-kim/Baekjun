from sys import stdin

num = list(stdin.readline().split())
x = int(num[0])
y = int(num[1])

if x > y : print(">")
elif x < y: print("<")
else : print("==")