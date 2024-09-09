n, k = map(int, input().split())
arr = list(map(int, input().split()))
if len(arr) != n:
    print("Invalid")
else:
    max_height = max(arr)
    if k >= max_height:
        print(0)
    else:
        print(max_height - k)