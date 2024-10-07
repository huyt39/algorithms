dish = list(map(int, input().split()))

division = 0
s_anna = 0
avr_anna = 0

if len(dish) != 2:
    print("Error")
else:
    cosh = list(map(int, input().split()))
    if len(cosh) != dish[0]:
        print("Error")
    else:
        division = int(input())

    
    for i in range(dish[0]):
        if i != dish[1]:
            s_anna += cosh[i]

    
    avr_anna = s_anna//2

    if (division == avr_anna):
        print("Bon Appetit")
    else:
        print(abs(avr_anna - division))






    