n = int(input())
chocolate = list(map(int, input().split()))

def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1

    return count

if len(chocolate) != n:
    print("error")
else:
    birth = list(map(int, input().split()))
    if len(birth) != 2:
        print("error")
    else:
        print(birthday(chocolate, birth[0], birth[1]))
    