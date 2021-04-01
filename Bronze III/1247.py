from sys import stdin
import time
start = time.time()

added = []
result = []
for _ in range(3):
    N = int(stdin.readline())
    added.append(0)
    for n in range(N):
        added[_] += int(stdin.readline())
    if added[_] == 0: 
        result.append('0')
    elif added[_] > 0:
        result.append('+')
    else:
        result.append('-')

for _ in range(3):
    print(result[_])          
print("time: ", time.time()-start)

