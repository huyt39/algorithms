n = int(input())

array = []

for i in range(n):
    arr = list(map(int, input().split()))
    array.append(arr)

if len(arr) != n:
    print("Error")
else:
    sum_left = 0
    sum_right = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                sum_left += array[i][j]
            if i + j == (n - 1):
                sum_right += array[i][j]
    diagonal_difference = abs(sum_left - sum_right)
    print(diagonal_difference)
    

