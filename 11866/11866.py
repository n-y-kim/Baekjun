from sys import stdin

def resultPrint():
    print("<", end='')
    for _ in result:
        if _ == result[n-1]: print(str(_) + ">")
        else: print(str(_)+ ", ",end='')

n, k = map(int,stdin.readline().split())
jesephus = [i for i in range(1,n+1)]
result = []

currentPosition = 0
willDelete = 0
while len(jesephus) != 0:
    willDelete = currentPosition + (k-1)
    while willDelete >= len(jesephus):
        willDelete = willDelete - len(jesephus)
    result.append(jesephus[willDelete])
    del jesephus[willDelete]
    currentPosition = willDelete

resultPrint()