num = int(input())
tops = list(map(int, input().split()))

stack = []  # (탑 높이, 탑 번호)
result = []

for i in range(num):
    while stack and stack[-1][0] < tops[i]:
        stack.pop()
    
    if stack:
        result.append(stack[-1][1])
    else:
        result.append(0)
    
    stack.append((tops[i], i + 1))  # 탑 번호는 1부터 시작

print(*result)