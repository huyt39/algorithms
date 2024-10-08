days = list(map(int, input().split()))

beautiful_days = 0

def reversed(n):
    reverse = str(n)[::-1]
    return int(reverse)

if len(days) != 3:
    print("Error")
else:
    for i in range(days[0], days[1] + 1):
        reverse = reversed(i)
        if abs(i - reverse) % days[2] == 0:
            beautiful_days += 1

    print(beautiful_days)
