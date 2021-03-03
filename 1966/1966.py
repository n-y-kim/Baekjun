from sys import stdin

def search(n,m):
    i = 0
    while i != n:
        j = i
        while j != n:
            if queue[i] < queue[j]:
                queue.append(queue.pop(0))
            else:
                queue.pop(0)
                break
            j+=1
        i+=1

x = int(stdin.readline())
while x > 0:
    n, m = map(int, stdin.readline().split())
    queue = list(map(int,stdin.readline().split()))``
    search(n,m)
    print(queue)
    x-=1

