from sys import stdin
n = int(stdin.readline())
arrayWanted = list()
array = list()
plusMinus = list()

for i in range(0,n): 
    x = int(stdin.readline())
    arrayWanted.append(x)

#print(arrayWanted)
i = 0
j = 1
array.append(j)
plusMinus.append("+")
j+=1

while i != n:
    if len(array)!=0 and array[-1] == arrayWanted[i]:
        array.pop(-1)
        plusMinus.append("-")
        i+=1
    elif j == n+1:
        print("NO")
        exit()
    elif len(array) == 0 or array[-1] != arrayWanted[i]:
        array.append(j)
        plusMinus.append("+")
        j+=1

for _ in plusMinus:
    print(_)