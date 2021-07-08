from sys import stdin
N = int(stdin.readline())
nums = [0, 1, 1]
for i in range(3, N+1):
    nums.append(nums[i-1] + nums[i-2])

print(nums[N])