from sys import stdin
import copy

N = int(stdin.readline())
nums = [0 for i in range(N)]
n = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0] #0부터 9까지 쪼개질 수 있는 범위, 마지막은 임의의 숫자 10이 쪼개질 수 있는 수, 즉 계속 0
for i in range(N):
    if i == 0: nums[0] = 9
    elif i == 1: nums[1] = 17
    else: 
        temp = copy.deepcopy(n)
        for j in range(1, 10):
            n[j] = temp[j-1] + temp[j+1]
            nums[i] += n[j]
        n[0] = n[9]
print(nums[N-1]%1000000000)