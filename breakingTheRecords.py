games = int(input())

points = list(map(int, input().split()))
best = points[0]
worst = points[0]
best_count = 0
worst_count = 0

if len(points) != games:
    print("Error")
else:
    for i in range(1, games):
        if points[i] > best:
            best_count += 1
            best = points[i]

    for j in range(1, games):
        if points[j] < worst:
            worst_count += 1
            worst = points[j]


    print(best_count, worst_count)

