# 22.06.13 / 이것이 코딩 테스트다 / 문자열 재정렬
###############################################################

# 내 코드

code = list(map(str, input()))
# print("code : ", code) 
str_list = [i for i in code if ord(i) >= 65]
# print("str_list : ", str_list)
int_list = [int(i) for i in code if ord(i) < 65]
# print("sum(int_list) : ", str(sum(int_list)))
result = ''.join(sorted(str_list)) + str(sum(int_list))
print(result)

###############################################################

# 저자 코드

data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
  # 알파벳이면 리스트에 삽입
  if x.isalpha():
    result.append(x)
  # 숫자는 따로 더하기
  else:
    value += int(x)

# 알파벳을 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 맨 뒤에 삽입
if value != 0:
  result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
