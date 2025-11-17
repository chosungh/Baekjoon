num = int(input())
num_arr = []

for i in range(num):
    num_arr.append(int(input()))

for i in range(num):
    for j in range(i+1, num):
        if num_arr[i] >= num_arr[j]:
            temp = num_arr[i]
            num_arr[i] = num_arr[j]
            num_arr[j] = temp

for i in num_arr:
    print(i)