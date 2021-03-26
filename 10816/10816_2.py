from sys import stdin

n = int(stdin.readline())
cardHave = list(map(int,stdin.readline().split()))
cardHave.sort()

m = int(stdin.readline())
cardNeedMatch = list(map(int,stdin.readline().split()))

result = {}
for card in cardHave:
    try:
        result[card] += 1
    except:
        result[card] = 1

for card in cardNeedMatch:
    try:
        print(result[card], end=' ')
    except:
        print(0, end=' ')