num = int(input())

for i in range(num):
    n = int(input())
    dp = [0] * (n+1)
    if n < 3:
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

    for j in range(3, n+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

    print(dp[n])