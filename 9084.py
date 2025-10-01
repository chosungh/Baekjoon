# 우리나라 화폐단위, 특히 동전에는 1원, 5원, 10원, 50원, 100원, 500원이 있다. 
# 이 동전들로는 정수의 금액을 만들 수 있으며 그 방법도 여러 가지가 있을 수 있다.
# 예를 들어, 30원을 만들기 위해서는 
# 1원짜리 30개 또는 10원짜리 2개와 5원짜리 2개 등의 방법이 가능하다.
# 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오.


#방법 (1) 1차원 dp--------------------------------------------------------------------
num = int(input())

for i in range(num):
    coin_num = int(input())
    coins = list(map(int, input().split()))[:coin_num]
    money = int(input())
    dp = [0] * (money+1) #money까지의 가지 수를 구해야 하기 때문에 dp = [0] * (money + 1)
    dp[0] = 1 #0원을 만드는 가지 수는 1개

    for coin in coins: #각각의 화폐 단위로 만들 수 있는 가지 수를 구하기 위함
        for j in range(coin, money+1): #사용하고자 하는 화폐 단위보다 작은 액수는 가지수를 구할 수 없기에 범위가 (coin, money +1)
            dp[j] += dp[j- coin] #j원을 만들려면, j-coin원을 만든 뒤 coin 하나를 더 쓰는 경우를 더해줌


print(dp[money])

#방법 (2) 2차원 dp(1차원 dp에 비해 비효율적)--------------------------------------------------------------------
num = int(input())
for _ in range(num):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1   # 0원을 만드는 방법은 항상 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i-1][j]
            if j - coins[i-1] >= 0:
                dp[i][j] += dp[i][j - coins[i-1]]

    print(dp[n][m])