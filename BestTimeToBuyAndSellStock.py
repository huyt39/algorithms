n = int(input())
prices = []
for i in range(n):
    value = int(input())
    prices.append(value)

min_value = min(prices)
max_value = max(prices)

min_pos = prices.index(min(prices))
max_pos = prices.index(max(prices))

profit = 0

if (min_pos < max_pos):
    profit = max_value - min_value

print(profit)

