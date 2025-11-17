num = int(input())
par_arr = []
result_arr = []

for i in range(num):
    par_arr = list(input())
    cnt = 0
    is_vps = True  

    for i in range(len(par_arr)):
        if par_arr[i] == ')':
            cnt -= 1
            if cnt < 0:
                is_vps = False
        elif par_arr[i] == '(':
            cnt += 1
   
    if cnt == 0 and is_vps == True:
        result_arr.append('YES')
    else : 
        result_arr.append('NO')

for i in result_arr:
    print(i)