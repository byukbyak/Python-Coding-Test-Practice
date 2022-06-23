# 리스트
a = [1, 4, 3]
print("기본 리스트 : ", a)

a.append(2)
print("삽입 : ", a)

a.sort()
print("오름차순 정렬 : ", a)

a.sort(reverse=True)
print("내림차순 정렬 : ", a)

b = [4, 3, 2, 1]

# 리스트의 원소 뒤집기
b.reverse()
print("원소 뒤집기 : ", b)

# 특정 인덱스에 값 추가
b.insert(2, 3)
print("인덱스 2에 3 추가 : ", b)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", b.count(3))

# 특정 값 데이터 삭제
b.remove(1)
print("값이 1인 데이터 삭제 : ", b)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

###################################################

# 딕셔너리
a = dict()
a['first'] = 1
a['second'] = 2

print(a)

b = {
  'first':1,
  'second':2
}

print(b)
print(b['second']) # 2

a_key_list = a.keys() # dict_keys(['first', 'second'])
b_key_list = list(b.keys()) # ['first', 'second']

print(a_key_list)
print(b_key_list)
