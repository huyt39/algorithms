import math


n = int(input())
for i in range(n):
    count = 0
    test = list(map(int, input().split()))
    if len(test) != 2:
        print("Error")
    else:
        for j in range(test[0], test[1] + 1):
            if(j % math.sqrt(j) == 0):
                count += 1
    print(count)



    
