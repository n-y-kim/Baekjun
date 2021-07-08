from sys import stdin
N = int(stdin.readline())
sums = [0 for i in range(N+1)]
dp = [[0], [1 for i in range(10)]]
for i in range(1, N+1):
    if i == 1:
        sums[i] = 1*10
    else:
        dp.append([0 for i in range(10)])
        for j in range(10):
            for k in range(j, 10):
                dp[i][j] += dp[i-1][k]
            sums[i] += dp[i][j]
print(sums[N]%10007)