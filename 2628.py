row, col = map(int, input().split())
num = int(input())
cut_arr = []
sum = 0
sum_list = []

for i in range(num):
    cut_arr.append(list(map(int,input().split())))

matrix = [[1 for _ in range(row)] for _ in range(col)]

for i in range(len(cut_arr)):
    if cut_arr[i][0] == 0:
        matrix.insert(cut_arr[i][1],[0 for _ in range(row)])
    elif cut_arr[i][0] == 1:
        for j in range(len(matrix)):
            matrix[j].insert(cut_arr[i][1], 0)

for i in range(len(matrix)):
    if matrix[i].count(0) >= row:
        sum_list.append(sum)
        sum = 0
        continue
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            sum += 1
        else: 
            break

print(sum_list)