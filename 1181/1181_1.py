from sys import stdin

N = int(stdin.readline())
wordDic = {}
for i in range(N):
    arr = list(stdin.readline())
    arr.pop()
    arr_l = len(arr)

    wordDic["".join(arr)] = arr_l

wordArr = wordDic.keys()
result = []
# for i in range(len(wordDic)):
#     for j in range(len(wordDic)):
#         if wordDic
print(wordDic)

print(wordDic.values())

a = 'can'
b = 'cap'

print(a>b)