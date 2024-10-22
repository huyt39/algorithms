n = int(input())

step = list((input()))

couting_valleys = 0
level = 0

for i in range(n):
    if step[i] == 'U':
        level += 1
    elif step[i] == 'D':
        level -= 1

    if step[i] == 'U' and level == 0:
        couting_valleys += 1

print(couting_valleys)