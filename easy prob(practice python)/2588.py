x, y = map(int, input().split())
first = int(y/100)
second = int((y-first*100)/10)
third = int((y-first*100-second*10))
print(x*third, x*second, x*first, x*y)