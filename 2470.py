# def data_sum_min(arr:list, left:int, right:int):
#     if left >= right:
#         return arr[left], arr[right]
    
#     sum_arr = [arr[left], arr[right]]
#     sum1 = sum(sum_arr)

#     print(sum_arr)

#     if sum1 == 0:
#         return sum_arr[0], sum_arr[1]
    
#     if abs(sum1) >= abs(arr[left] + arr[right]):
#         sum_arr = [arr[left] + arr[right]]
    
#     if sum1 > 0:
#         return data_sum_min(arr, left, right-1)
#     elif sum1 == 0:
#         return arr[left], arr[right]
#     else: return data_sum_min(arr, left+1, right)

num = int(input())
data = list(map(int, input().split()))[:num]
left = 0
right = num-1
data.sort()
sum1 = abs(data[left] + data[right]) #맨 첫번째 수와 마지막 수를 합해서 절댓값을 구함
result = [data[left], data[right]] #맨 첫번째 수와 마지막 수를 배열에 삽입

while 1: 
    if left >= right: #기저 조건
        break

        
    if abs(data[left]+data[right]) < sum1: #만약 data[left]값과 data[right]값의 합이 sum1보다 작다면
        sum1 = abs(data[left]+data[right]) #sum1을 그 값으로 변환 왜? 우리는 이 수들의 합이 가장 0에 가까운 걸 찾아야 하기 때문에
        result = [data[left], data[right]] #그래서 data[left]와 data[right]도 배열에 집어넣음

    if sum1 == 0: #만약 sum1이 0이라면 더 이상 찾을 필요 없으니 break
        break

    if data[left] + data[right] > 0: #만약 두 수의 합이 0보다 크면 양의 정수가 음의 정수에 비해 크다는 의미
        right -=1 #그래서 right-1을 통해 정렬되어 있는 배열에서 right보다 작은 수를 설정
    elif data[left] + data[right] < 0:
        left += 1

print(f"{result[0]} {result[1]}")