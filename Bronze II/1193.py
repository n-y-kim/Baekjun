from sys import stdin

def repeat(R):
    for word in S_list:
        print(word*R, end="")
    print()

T = int(stdin.readline())
for i in range(T):
    R, S = stdin.readline().split()
    R = int(R)
    S_list = list(S)

    repeat(R)
    