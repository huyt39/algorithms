year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Co")
else:
    du = year % 4
    print("Khong, " + str(year + (4 - du)))
