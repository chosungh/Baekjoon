num = int(input())
money = 1000 - num
coins = [500, 100, 50, 10, 5, 1]
res = []

for coin in coins:
    res.append(money // coin)
    money %= coin
    if money == 0:
        break

print(sum(res))