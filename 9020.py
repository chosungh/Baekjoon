def is_prime_num(n):
    arr = [True] * (n + 1) # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True: # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i*j] = False # i의 배수의 값을 False로 지워준다.
                j += 1
    return arr

def is_prim_num_sum(arr: int, num: int, prime_num_arr: list):
    arr_center = int(len(prime_num_arr)/2)
    prime_num1 = 0
    prime_num2 = 0


    for j in range(0, arr_center+1, 1):
        prime_num1 = arr_center-j
        prime_num2 = arr_center+j

        if prime_num_arr[prime_num1] == True and prime_num_arr[prime_num2] == True:
            break

    print(prime_num1, prime_num2)

num = int(input())
arr = []
prime_num_arr = []

for i in range(num):
    arr.append(int(input()))

for i in range(num):
    prime_num_arr.append(is_prime_num(arr[i]))

for i in range(num):
    is_prim_num_sum(arr[i], num, prime_num_arr[i])