# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 
# 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

parts = input().split('-') #-를 기준으로 문자열을 나눔

first_sum = sum(map(int, parts[0].split('+'))) # 첫 번째 part는 무조건 -의 왼쪽이기에 더하기 밖에 없음

rest_sum = 0
for part in parts[1:]: #2번째 part부터 반복문을 돌림
    rest_sum += sum(map(int, part.split('+'))) #+를 기준으로 문자열을 나눠서 합한 값을 rest_sum에 저장

result = first_sum - rest_sum
print(result)