from sys import stdin

firstL = list(stdin.readline())
firstL.pop()
secondL = []

m = int(stdin.readline())
for i in range(0,m):
    command = list(stdin.readline())
    if command[0] == 'L':
        if len(firstL) == 0: continue
        else: secondL.append(firstL.pop())
    elif command[0] == 'D':
        if len(secondL) == 0: continue
        else: firstL.append(secondL.pop())
    elif command[0] == 'B':
        if len(firstL) == 0: continue
        else: firstL.pop()
    else:
        addLetter = command[2]
        firstL.append(addLetter)

secondL.reverse()

arr = firstL+secondL

for letter in arr:
    print(letter, end='')

print()
