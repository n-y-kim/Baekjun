from sys import stdin
n = int(stdin.readline())
arrayWanted = list()
array = list()
plusMinus = list()

for i in range(0,n): 
    x = int(stdin.readline())
    arrayWanted.append(x)

print(arrayWanted)
i = 0
j = 0
popNum = arrayWanted[0]
array.append(j)
plusMinus.append("+")

while True :
    if len(array)!=0 and popNum == array[i] :
        print("first")
        array.pop(-1)
        plusMinus.append("-")
        
        if len(array) == 0 and i == n-1: exit()
        elif len(array) == 0: popNum += 1
        else: popNum = array[-1]

        print("i: %d popNum: %d" %(i,popNum))
        i-=1
    else:
        if j > n and len(array) != 0:
            print("NO")
            exit()
        elif j > n and len(array) == 0:
            break
        else: # j != arrayWanted[i]
            print("second")
            print("i: %d j: %d" %(i,j))
            j+=1
            i+=1
            array.append(j)
            plusMinus.append("+")
            popNum = array[-1]

for _ in plusMinus:
    print(_)