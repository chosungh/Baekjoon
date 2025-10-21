a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)

num_list = list(map(int, result))
num_list_length = len(num_list)
num_count = [0,0,0,0,0,0,0,0,0,0]


for i in range(num_list_length):
    if num_list[i] == 0: num_count[0] += 1
    if num_list[i] == 1: num_count[1] += 1
    if num_list[i] == 2: num_count[2] += 1
    if num_list[i] == 3: num_count[3] += 1
    if num_list[i] == 4: num_count[4] += 1
    if num_list[i] == 5: num_count[5] += 1
    if num_list[i] == 6: num_count[6] += 1
    if num_list[i] == 7: num_count[7] += 1
    if num_list[i] == 8: num_count[8] += 1
    if num_list[i] == 9: num_count[9] += 1

for i in range(len(num_count)):
    print(num_count[i])