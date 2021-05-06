from sys import stdin

N, M = map(int, stdin.readline().split())
notHeardOrSeen = []
totalNum = 0
total = []
result = []

for i in range(N):
    notHeardOrSeen.append(str(stdin.readline()))

for j in range(M):
    notHeardOrSeen.append(str(stdin.readline()))

notHeardOrSeen.sort()

for i in range(N+M):
    if i != N+M-1 and notHeardOrSeen[i] == notHeardOrSeen[i+1]:
        total.append(notHeardOrSeen[i])
        totalNum+=1

print(totalNum)

for i in range(len(total)):
    result = list(total[i])
    result.pop()
    for r in result:
        print(r, end='')
    print()

