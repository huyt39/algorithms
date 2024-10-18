string = (input())
count = 1
for char in range(1, len(string)):
    if string[char].isupper() == True:
        count += 1

print(count)