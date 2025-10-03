def binary_sort(num:int ,arr:list, left:int, right:int):
    if left > right:
        return 0
    
    mid = (left + right) // 2

    if num == arr[mid]:
        return 1
    
    elif num > arr[mid]:
        return binary_sort(num, arr, mid+1, right)
    
    elif num < arr[mid]:
        return binary_sort(num, arr, left, mid-1)

num1 = int(input())
num_arr1 = []
num_arr2 = []

num_arr1 = list(map(int, input().split()))[:num1]

num2= int(input())
num_arr2 = list(map(int, input().split()))[:num2]

num_arr1.sort()

for i in range(len(num_arr2)):
    print(binary_sort(num_arr2[i], num_arr1, 0, len(num_arr1)-1))