from sys import stdin

def findPoint(num):
    for i in range(len(addedArray)):
        if num > addedArray[i] and num < addedArray[i+1]:
            return i+1, num - (addedArray[i]);
        elif num == addedArray[i]:
            return i+1, 0

        
def returnTest():
    return 1, 2

addedArray = []

for i in range(1, 45):
    addedArray.append(i*(i+1)//2)

print(addedArray)

A, B = map(int, stdin.readline().split())
A_previousNum, A_alphaNum = findPoint(A)
B_previousNum, B_alphaNum = findPoint(B)

print("%d %d %d %d" %(A_previousNum, A_alphaNum, B_previousNum, B_alphaNum))

result = 0
for i in range(A_previousNum, B_previousNum+2):
    if i == A_previousNum: 
        if A_alphaNum == 0: result += i
        else: result += (i+1) * (i+1-(A_alphaNum-1))
        print(result)
    elif i == B_previousNum:
        if B_alphaNum == 0: result += i * i
        else: result += (i+1) * B_alphaNum
        print(result)
    else:
        result += i * i
        print(result)


print(result)


