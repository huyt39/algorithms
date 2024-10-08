money = list(map(int, input().split()))
most_expensive = 0
if len(money) != 3:
    print("Error")
else:
    keyboard = list(map(int, input().split()))
    if len(keyboard) != money[1]:
        print("Error")
    else:
        drives = list(map(int, input().split()))
        if len(drives) != money[2]:
            print("Error")
        else:
            for i in range(money[1]):
                for j in range(money[2]):
                    if keyboard[i] + drives[j] <= money[0] and keyboard[i] + drives[j] > most_expensive:
                        most_expensive = keyboard[i] + drives[j]
        
        if (most_expensive > 0):
            print(most_expensive)
        else:
            print(-1)

