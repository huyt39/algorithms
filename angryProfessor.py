t = int(input())
onTime =[]

for a in range(t):
    n, k = map(int, input().split())
    students = list(map(int, input().split()))
    if len(students) != n:
        print("Error")
    else:
        for j in range(n):
            if students[j] <= 0:
                onTime.append(students[j])
        if len(onTime) < k:
            print("YES")
        else:
            print("NO")
    onTime.clear()
    
    