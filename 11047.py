# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

num, k = map(int, input().split())
coins = []
sum = 0

for i in range(num):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in range(num):
    sum += k // coins[i] #큰 화폐단위로 나누었을 때 몫이 있다면 동전 갯수의 최솟값을 구하는 것이기 때문
    k %= coins[i] #나머지는 이 화폐단위보다 작은 돈이기에 더 작은 화폐로 지불해야 함

print(sum)