from collections import Counter
n = int(input())

birds = list(map(int, input().split()))

frequently = []

if len(birds) != n:
    print("Error")
else:
    counter = Counter(birds)
    max_count = max(counter.values())
    max_type = [k for k, v in counter.items() if v == max_count]

    max_type.sort()
    print(max_type[0])