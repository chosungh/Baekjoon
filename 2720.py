num = int(input())
coins = [25, 10, 5, 1]
res = []

for i in range(num):
    c = int(input())
    for coin in coins:
        res.append(c // coin)
        c %= coin

print(*res)