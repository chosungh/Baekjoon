num1 = int(input())
num2 = input()
mulList = []
sum = 0

num2List = [int(i) for i in num2]

for i in range(3, 0, -1):
    mulList.append(num1 * num2List[i-1])
    print(num1 * num2List[i-1])

for i in range(0, 3, 1):
    sum += (int(str(mulList[i])+"0"*i))

print(sum)