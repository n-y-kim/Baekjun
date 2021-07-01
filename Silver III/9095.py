from sys import stdin
t = int(stdin.readline())
cases = [1, 2, 4]
for i in range(7): cases.append(0)
for i in range(t):
    test = int(stdin.readline())
    for j in range(3, test): cases[j] = cases[j-1]+cases[j-2]+cases[j-3]
    print(cases[test-1])
