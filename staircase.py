n = int(input())


for i in range (n):
    for j in range(n):
        if j in range(n - i - 1, n):
            print("#", end = "")
        else:
            print(" ", end = "")
    print()