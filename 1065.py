num = int(input())
count = 0
num_list = []

for i in range(1, num+1):
    if i < 100:
        count += 1
        continue
    else:
        num = list(map(int, str(i)))
        if len(num) == 3:
            if num[0] - num[1] == num[1] - num[2]:
                count += 1
        elif len(num) == 4:
            if num[0] - num[1] == num[1] - num[2] and num[0] - num[1] == num[2] - num[3]:
                count += 1

print(count)   