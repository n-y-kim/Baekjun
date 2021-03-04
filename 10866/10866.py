from sys import stdin

def push_front(num):
    x.insert(0,num)

def push_back(num):
    x.append(num)

def pop_front():
    if len(x) == 0: print("-1")
    else: print(x.pop(0))

def pop_back():
    if len(x) == 0: print("-1")
    else: print(x.pop(-1))

def size():
    print(len(x))

def empty():
    if len(x) == 0 : print("1")
    else: print("0")

def front():
    if len(x) == 0: print("-1")
    else: print(x[0])

def back():
    if len(x) == 0: print("-1")
    else: print(x[-1])

n = int(stdin.readline())
x = []
func = []
functions = {'pop_front': pop_front, 'pop_back': pop_back, 'size': size, 'empty': empty, 'front': front, 'back': back}

for _ in range(n):
    func = list(stdin.readline().split())
    if func[0] == 'push_front': push_front(int(func[1]))
    elif func[0] == 'push_back': push_back(int(func[1]))
    else: 
        funcs = functions[func[0]]
        funcs()
