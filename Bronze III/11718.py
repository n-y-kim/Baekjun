from sys import stdin

for i in range(100):
    try:   
        newWords = stdin.readline()
        print(newWords, end='')
    except: break

# a = stdin.readline()
# b = stdin.readline()

# words = []
# words.append(a)
# words.append(b)

# print(words)

# for i in range(2):
#     print(words[i], end='')

# print(words[0][0])