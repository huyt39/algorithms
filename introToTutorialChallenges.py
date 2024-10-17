value = int(input())
n = int(input())

num = list(map(int, input().split()))

if len(num) != n:
    print("error")
else:
    for i in range(n):
        if num[i] == value:
            print(num.index(value))
            break
