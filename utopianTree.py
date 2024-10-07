def height(n):
    H = 0
    if n == 0:
        H = 1
    else:
        if n % 2 == 1:
            H = 2*height(n-1)
        else:
            H = height(n-1) + 1

    return H

t = int(input())
for i in range(t):
    n = int(input())
    print(height(n))
    