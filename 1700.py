import sys

input = sys.stdin.readline

holes, device_num = map(int, input().split()) 
devices = list(map(int, input().split()))
multi_tab = [0] * holes



print(devices)

# for i in range(num):
#     can_arr = []
#     num1 = int(input())
#     for j in range(num1):
#         a, b = map(int, input().split())
#         can_arr.append([a, b])
#     can_arr.sort()
#     result = can_arr[0][1]
#     cnt = 1

#     for j in range(1, num1):
#         if can_arr[j][1] < result:
#             result = can_arr[j][1]
#             cnt += 1

#     print(cnt)