# 지원자가 모두 한 장소에 모였다고 생각해 볼게요.

# 그 중에 한 지원자의 입장이 되어, 다른 지원자들의 면접, 서류 점수를 봅니다.

# 그 중에 어떤 한 사람이라도 나보다 두 점수가 더 높으면, 나는 선발이 안 됩니다.

# 그런 사람이 없으면 나는 선발되는 거고요.

# 이를 모든 지원자에 대해 다 해보는 것입니다.

from sys import stdin

a = []
passed = []
t = int(stdin.readline())

for i in range(0, t):
    passed.append(1)
    n = int(stdin.readline())
    for j in range(0,n):
        ranks = list(map(int, stdin.readline().split()))
        a.append(ranks)
    a.sort();
    
    min = a[0][1]

    for j in range(1, n):
        if a[j][1] < min:
            passed[i] += 1
            min = a[j][1]

    del a[0:]

for i in range(0,t):
    print(passed[i])