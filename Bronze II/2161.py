from sys import stdin
from collections import deque

N = int(stdin.readline())
cards = deque()
trashCards = []
for i in range(1,N+1): cards.append(i)

while len(cards) != 0:
    trashCards.append(cards.popleft())
    try:
        cards.append(cards.popleft())
    except: break

for card in trashCards:
    print("%d " %card, end="")