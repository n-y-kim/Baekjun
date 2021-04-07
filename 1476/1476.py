from sys import stdin

#1<E<15 / 1<E<28 / 1<M<19 다 이상 이하

E, S, M = map(int, stdin.readline().split())
resultYear = 1
if E == 15: E = 0
if S == 28: S = 0
if M == 19: M = 0
while True:
    if resultYear%15 == E and resultYear%28 == S and resultYear%19 == M:
        print(resultYear)
        exit()
    resultYear += 1
