num = int(input())
num_list = []

for i in range(num):
    num_list.append(int(input()))

num_list.sort()

for i in range(num):
    print(num_list[i])