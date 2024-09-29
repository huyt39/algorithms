time = str(input())

if len(time) != 10:
    print ('Error')
else:
    hour = int(time[:2])
    if time[8] == 'A' and hour < 12:
        print (time[:8])
    elif time[8] == 'A' and hour == 12:
        print(f"00{time[2:8]}")
    elif time[8] == 'P' and hour == 12:
        print(time[:8])
    elif time[8] == 'P' and int(time[:2]) < 12:
        hour += 12
        print(f"{hour}{time[2:8]}")