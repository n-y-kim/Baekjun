from sys import stdin

arr = list(stdin.readline())
arr.pop()
m = int(stdin.readline())
cursor = len(arr)

for i in range(0,m):
    command = list(stdin.readline())
    if command[0] == 'L':
        if cursor == 0: continue
        else: cursor -= 1

    elif command[0] == 'D':
        if cursor == len(arr): continue
        else: cursor += 1

    elif command[0] == 'B':
        if cursor == 0: continue
        elif cursor == len(arr): arr.pop()
        else:
            arr_1 = arr[0:cursor]
            arr_2 = arr[cursor:]

            try: arr_1.pop()
            except: arr_1 = arr_1
            arr = arr_1 + arr_2
        
        cursor -= 1

    else:
        addLetter = command[2]
        if cursor == len(arr):
            arr.append(addLetter)
        else:
            arr_1 = arr[:cursor]
            arr_2 = arr[cursor:]
            arr_1.append(addLetter)
            arr = arr_1+ arr_2

        cursor += 1

for letter in arr:
    print(letter,end='')
print()