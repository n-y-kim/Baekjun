from sys import stdin

x = int(stdin.readline())
temp = 4
counts = [0, 0, 1, 1]

while temp < x+1:
    if temp % 2 != 0:
        if temp % 3 != 0: #3의 배수가 아닌 홀수
            counts.append(counts[temp-1] + 1)
        elif temp % 3 == 0: #3의 배수인 홀수
            if counts[temp//3] < counts[temp-1] : counts.append(counts[temp//3] + 1)
            else: counts.append(counts[temp-1]+1)
    elif temp % 2 == 0: #짝수
        if temp % 3 == 0: #6의 배수
            if counts[temp-1] < counts[temp//3] and counts[temp-1] < counts[temp//2]: counts.append(counts[temp-1]+1)
            elif counts[temp//2] < counts[temp-1] and counts[temp//2] < counts[temp//3]: counts.append(counts[temp//2]+1)
            else: counts.append(counts[temp//3]+1)
        else: 
            if counts[temp//2] < counts[temp-1]: counts.append(counts[temp//2]+1)
            else: counts.append(counts[temp-1]+1)
    temp += 1

print(counts[x])