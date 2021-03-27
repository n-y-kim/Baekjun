from sys import stdin
T = int(stdin.readline())
result = []
for _ in range(0,T):
    a, b = map(int,stdin.readline().split())
    b = b % 4 + 4
    if a**b%10 == 0: result.append(10)
    else: result.append(a**b%10)
for r in result:
    print(r)

# 2 16 -> 6

# 1
# 2 4 8 6 2
# 3 9 7 1 3
# 4 6 4 6 4
# 5 
# 6
# 7
# 8
# 9 1 9 1
# 10
# 11
# 12