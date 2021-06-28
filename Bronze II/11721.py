from sys import stdin

words = stdin.readline()
loop = len(words)-1//10
if len(words)-1%10 != 0: loop+=1
for i in range(loop):
    for j in range(i*10, (i+1)*10):
        if j == len(words)-1 : 
            print()
            exit()
        print(words[j], end='')
    print()