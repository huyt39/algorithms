house = list(map(int, input().split()))
if len(house) != 2:
    print("Error")
else:
    tree = list(map(int, input().split()))
    if len(tree) != 2:
        print("Error")
    else:
        num = list(map(int, input().split()))
        if len(num) != 2:
            print("Error")
        else:
            apples = list(map(int, input().split()))
            oranges = list(map(int, input().split()))
            if len(apples) != num[0] or len(oranges) != num[1]:
                print("Error")
            else:
                for i in range(num[0]):
                    apples[i] += tree[0]
                for j in range(num[1]):
                    oranges[j] += tree[1]

            count_apples = 0
            count_oranges = 0

            for i in range(num[0]):
                if house[0] <= apples[i] and apples[i] <= house[1]:
                    count_apples += 1
            for j in range(num[1]):
                if house[0] <= oranges[j] and oranges[j] <= house[1]:
                    count_oranges += 1

            print(count_apples)
            print(count_oranges)


