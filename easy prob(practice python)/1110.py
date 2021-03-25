x = int(input())
cycle = 0
new = 0

if x == 0:
    cycle = 1

while new != x :
    if cycle == 0: 
        ten = int(x / 10)
        one = int(x % 10)
    else: 
        ten = int(new/10)
        one = int(new%10)

    newOne = ten + one
    if newOne >= 10:
        newOne = newOne % 10
    newTen = one

    new = newTen*10 + newOne
    cycle += 1

print(cycle)


