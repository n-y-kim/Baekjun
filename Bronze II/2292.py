from sys import stdin

N = int(stdin.readline())

#6의 배수로 한 층에 있는 개수가 늘어난다!
#1/6/12/18..
#1/2,3,4,5,6,7/8,9,10,...,19/20,..,37/38, ... ,61/

# 1 / .. 1+6 / .. 1+ 6+ 12 / ... 1 + 6 + 12 + 18/
# 1 / .. 1+ 6 / ... 1 + 6 + 6 + 6 / .. 1 + 6 + 6 + 6 + 6 + 6 + 6
# 1 / ...1 + 6*1 /1 + 6*1 + 6*2 / 
    
#6*(1 + 2 + 3 + ...)
#6 * n(n+1)/2 + 1
if N == 1: 
    print(N)
    exit()

for countRooms in range(1,1000000000//6):
    if N >= 6*(countRooms-1)*countRooms//2+2 and N < 6*countRooms*(countRooms+1)//2+2:
        print(countRooms+1)
        exit()

        
