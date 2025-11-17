num = int(input())

test_case = [list(map(int, input().split())) for _ in range(num)]
test_case_sum = []
test_case_avg = []
test_case_over_avg = []
test_case_over_avg_count = 0

for i in range(num):
    test_case_length = len(test_case[i])
    case_sum = 0
    for j in range(1, test_case_length, 1):
        case_sum += test_case[i][j]
    test_case_sum.append(case_sum)

for i in range(num):
    test_case_avg.append(test_case_sum[i] / test_case[i][0])

for i in range(num):
    test_case_over_avg_count = 0
    test_case_length = len(test_case[i])
    for j in range(1, test_case_length, 1):
        if test_case[i][j] > test_case_avg[i]:
            test_case_over_avg_count += 1
    test_case_over_avg.append(test_case_over_avg_count)

for i in range(num):
    print("{:.3f}%".format((test_case_over_avg[i]/(len(test_case[i])-1))*100))