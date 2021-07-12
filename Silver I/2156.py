from sys import stdin
import copy

n = int(stdin.readline())
init = [0]
for i in range(n):
    init.append(int(stdin.readline()))

dp = [0 for i in range(n+1)]
dp[1] = init[1]
if n >= 2: dp[2] = dp[1] + init[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+init[i-1]+init[i], dp[i-1], dp[i-2]+init[i])

print(dp[n])