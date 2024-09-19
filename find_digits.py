n = int(input())

arr = []

def find_digits(number):
    count = 0
    digits = [int(digit) for digit in str(number)]
    for j in range(len(digits)):
        if digits[j] == 0:
            continue
        elif number % digits[j] == 0:
            count+=1
    return count

for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n):
    print(find_digits(arr[i]))

