n = int(input())
if n % 2 == 0:
    print("error")
else:
    num = list(map(int, input().split()))
    if (len(num)!=n):
        print("error")
    else:
        num.sort()
        print(num[n//2])
        
        