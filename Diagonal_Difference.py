n = int(input())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

for row in arr:
    print(row)