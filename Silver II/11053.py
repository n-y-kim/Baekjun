from sys import stdin

n = int(stdin.readline())
a = []
a += list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)]
result = 0

for i in range(0, n):
    count = 0
    for j in range(0, i):
        if a[i] > a[j]: 
            if count < dp[j]: count = dp[j]
    dp[i] = count + 1
    result = max(dp[i], result)

print(result)