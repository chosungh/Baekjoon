num = int(input())
num_list = []

for i in range(num):
    num_list.append(input().split())

for i in range(num):
    for j in range(len(num_list[i][1])):
        print(num_list[i][1][j] * int(num_list[i][0]), end="")
    print()