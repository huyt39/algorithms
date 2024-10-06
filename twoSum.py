nums = list(map(int, input().split(",")))
target = int(input())
arr = []

for i in range(len(nums) - 1):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target:
            arr.append(i)
            arr.append(j)

arr1 = []

if len(arr) > 2:
    arr1.append(arr[0])
    arr1.append(arr[1])
    print(arr1)
else:
    print(arr)




            

