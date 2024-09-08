nums = []
n = int(input())
for i in range(n):
    value = int(input())
    nums.append(value)

for val in nums:
    if nums.count(val) == 1:
        print(val)