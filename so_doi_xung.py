def count_num(n, m):
    count = 0
    if n <= 100 or m >= 100000:
        return 'N/A'  
    for i in range(n, m + 1):
        if 100 < i < 1000:
            if i // 100 == i % 10:  
                count += 1
        elif 1000 < i < 10000:
            if (i // 1000 == i % 10) and ((i % 100) // 10 == (i // 100) % 10):
                count += 1
        elif 10000 < i < 100000:
            if (i // 10000 == i % 10) and ((i % 100) // 10 == (i // 1000) % 10):
                count += 1
    
    return count  

n = int(input())
m = int(input())
result = count_num(n, m)
print(result)  
