from sys import stdin

def searchFirst(searchingNum):
    foundedSpot = 0
    try:
        foundedSpot = cardHave.index(searchingNum)
    except:
        foundedSpot = -1
    return foundedSpot

def searchAfter(num):
    try:
        if cardHave[num+1] == cardHave[num]:
            return 1
        else:
            return 0
    except:
        return 0
    

n = int(stdin.readline())
cardHave = list(map(int,stdin.readline().split()))
cardHave.sort()

m = int(stdin.readline())
cardNeedMatch = list(map(int,stdin.readline().split()))

result = []
for _ in cardNeedMatch:
    spot = searchFirst(_)
    if spot == -1:
        result.append(0)
    else:


for _ in result:
    print("%d " %(_), end='')
print()