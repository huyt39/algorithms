age = int(input())

candles = list(map(int, input().split()))

tallest = max(candles)
Count = candles.count(tallest)

print(Count)



