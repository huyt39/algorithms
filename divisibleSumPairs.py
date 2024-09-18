n, k = map(int, input().split())

count = 0
arr = []

arr = list(map(int, input().split()))

if len(arr) != n:
    print('Error!')
else:
    for i in range(n - 1):
        for j in range(i+1, n):
            if(arr[i] + arr[j]) % k == 0:
                count += 1

print(count)