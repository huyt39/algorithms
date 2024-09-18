n = int(input())

arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n):
    if arr[i] < 38:
        print(arr[i])
    else:
        if (arr[i] + 1) % 5 == 0:
            print(arr[i] + 1)
        elif (arr[i] + 2) % 5 == 0:
            print(arr[i] + 2)
        else:
            print(arr[i])
