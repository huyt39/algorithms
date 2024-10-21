n = int(input())
colors = list(map(int, input().split()))
pairs = 0
from collections import Counter

if len(colors) != n:
    print("error")
else:
    color_count = Counter(colors)
    for count in color_count.values():
        pairs += count//2
    print(pairs)

