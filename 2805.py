def binary_sort(num:int, arr:list, left:int, right:int):
    trees_sum = 0

    if left > right:
        return right
    
    mid = (left + right) //2

    for i in range(len(arr)):
        if mid > arr[i]:
            continue

        trees_sum += arr[i] - mid

    if trees_sum >= num:
        return binary_sort(num, arr, mid+1, right)
    else:
        return binary_sort(num, arr, left, mid-1)
        


trees, trees_hieght = map(int, input().split())
trees_arr = list(map(int, input().split()))[:trees]

trees_arr.sort()

print(binary_sort(trees_hieght, trees_arr, 0, max(trees_arr)))