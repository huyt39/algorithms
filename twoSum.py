nums = list(map(int, input().split(",")))
target = int(input())
arr = []

for i in range(len(nums) - 1):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target:
            arr.append(i)
            arr.append(j)

print(arr)