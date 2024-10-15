n = int(input())

num = list(map(int, input().split()))


if len(num) != n:
    print("error")
else:
    freg = {}
    for i in num:
        if i in freg:
            freg[i] += 1
        else:
            freg[i] = 1

    max_frequency = max(freg.values())
    print(n - max_frequency)
