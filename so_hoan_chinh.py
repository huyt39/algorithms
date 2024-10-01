def check(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i 

    if s == num:
        return True
    
def check_a_b(num):
    if num in range(a, b+1):
        return True
    else:
        return False

n = int(input())
arr = []
if n<=1 or n >= 100000:
    print('NA')
for i in range(1, n+1):
    if(check(i) == True):
        arr.append(i)

arr.sort()
print(arr)
    
