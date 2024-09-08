n = int(input())
arr = list(map(int, input().split()))
neg = 0
pos = 0
zeros = 0
for val in arr:
    if val > 0:
        pos += 1
    elif val == 0:
        zeros += 1
    else:
        neg += 1
pos_rate = pos/n 
neg_rate = neg/n
zeros_rate = zeros/n

print(pos_rate)
print(neg_rate)
print(zeros_rate)