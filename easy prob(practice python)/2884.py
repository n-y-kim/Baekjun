from sys import stdin
h, m = map(int, stdin.readline().split())
if m-45 < 0 :
    m = 60 + (m-45)
    if h == 0 : h = 23
    else: h -= 1
else : m -= 45

print(str(h)+" "+str(m))