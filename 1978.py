num = int(input())
num_list = list(map(int, input().split()))[:num]
count = 0

for i in range(num):
    if num_list[i] < 2: 
        continue
    is_prime = True
    for j in range(2, num_list[i]):
        if num_list[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print(count)