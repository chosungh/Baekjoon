from collections import deque

num = int(input()) #5를 입력받았다고 가정
q = deque()

for i in range(num):
    q.append(i+1)

while 1:
    if len(q) == 1:
        break
    else:
        q.popleft() #[1, 2, 3, 4, 5]여기서 1을 삭제
        q.append(q.popleft())   #[2, 3, 4, 5]여기서 2를 삭제하고 append를 통해서 맨 뒤로 보냄

print(q[0])