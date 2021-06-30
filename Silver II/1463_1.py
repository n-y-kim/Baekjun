from sys import stdin

x = int(stdin.readline())
temp = 4
counts = [0, 0, 1, 1]

while temp < x+1:
    counts.append(counts[temp-1]+1)
    if temp % 2 == 0 and counts[temp] > counts[temp//2] + 1:
        counts[temp] = counts[temp//2]+1
    if temp % 3 == 0 and counts[temp] > counts[temp//3] + 1:
        counts[temp] = counts[temp//3]+1
    temp+=1

print(counts[x])