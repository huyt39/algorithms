n = int(input())

cumulative = 0

if n == 1:
    share = 5
    like = 5 // 2
    cumulative += like 
    print(cumulative)

else:
    share = 5
    like = 5 // 2
    cumulative += like
    for i in range(2, n + 1):
        share = like*3
        like = share // 2
        cumulative += like

    print(cumulative)

