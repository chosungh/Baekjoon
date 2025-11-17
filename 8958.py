num = int(input())

quizes = [list(input().strip()) for _ in range(num)]

for i in range(num):
    quizesitemlength = len(quizes[i])
    for j in range(quizesitemlength):
        if quizes[i][j] == 'O':
            quizes[i][j] = 1
        else:
            quizes[i][j] = 0

for i in range(num):
    quizesitemlength = len(quizes[i])
    for j in range(quizesitemlength):
        if j == 0:
            if quizes[i][j] == 1:
                quizes[i][j] = 1
            else:
                quizes[i][j] = 0
        else:
            if quizes[i][j] == 1:
                quizes[i][j] += quizes[i][j-1]
            else:
                quizes[i][j] = 0

for i in range(num):
    print(sum(quizes[i]))