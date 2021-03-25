from sys import stdin

# def bubbleSort(num):
#     for index in range(0,num-1):
#         if x[index] > x[index+1]:
#             temp = x[index+1]
#             x[index+1] = x[index]
#             x[index] = temp

n = int(stdin.readline())
x = list(map(int,stdin.readline().split()))

print("%d %d" %(min(x), max(x)))


# for minus in range(0,n):
#     if minus == n: break
#     bubbleSort(n - minus)

# print("%d %d" %(x[0], x[-1]))