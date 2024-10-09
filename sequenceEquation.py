n = int(input())

num = list(map(int, input().split()))

if len(num) != n:
    print("Error")
else:
    for x in range(1, n+1):
        index1 = num.index(x)
        index1 += 1
        index2 = num.index(index1)
        index2 += 1
        print(index2)