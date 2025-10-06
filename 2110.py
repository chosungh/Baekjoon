def router_dis(n:int, arr:list, left:int, right:int):
    mid = (left + right) // 2 #첫번째 집과 마지막 집의 거리의 중간
    result = arr[0] #공유기를 설치한 첫번째 집 위치
    cnt = 0 
    cnt += 1 #공유기를 설치했기에 +1

    if left > right: #기저 조건
        return mid #거리

    for i in range(1, len(arr)): #배열의 길이만큼 반복
        if arr[i] - result >= mid: #만약 i번째 집의 위치와 공유기를 설치한 집과의 거리가 mid보다 크면
            cnt += 1 #cnt +1
            result = arr[i] #마지막으로 공유기 설치한 집 위치
            continue
        elif arr[i] - result < mid: #만약 1번째 위치와 공유기를 설치한 집과의 거리가 Mid보다 작다면
            continue #다음 집으로 넘어감
    
    if cnt >= n: #만약 cnt가 설치할 공유기 수보다 많거나 같으면 거리가 짧다는 소리
        return router_dis(n, arr, mid+1, right) #그래서 left를 mid+1로 바 꿈
    else: return router_dis(n, arr, left, mid-1) #아닐 경우엔 거리가 멀다는 소리 그래서 Right를 mid-1로 바꿈

house_num, router_num = map(int, input().split())
house_arr = []

for i in range(house_num):
    house_arr.append(int(input()))

house_arr.sort()

print(router_dis(router_num, house_arr, 0, (house_arr[-1] - house_arr[0])))