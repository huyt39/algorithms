arr = list(map(int, input().split()))

arr.sort()
max_sum = 0
min_sum = 0

if len(arr) != 5:
    print('Error')
else:
    for i in range(4):
        min_sum += arr[i]
    for j in range(1, 5):
        max_sum += arr[j]

print(str(min_sum)+" "+str(max_sum))