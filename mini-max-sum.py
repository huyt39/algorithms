n = int(input())
arr = []
for i in range(n):
    val = int(input())
    arr.append(val)
    
arr.sort()
sum = 0
for val in arr:
    sum += val 

sum_min = sum - arr[n-1]
sum_max = sum - arr[0]

print(str(sum_min)+' '+str(sum_max))