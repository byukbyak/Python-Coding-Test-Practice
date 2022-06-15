# 배열의 크기 n 숫자가 더해지는 횟수 m, 같은 수를 한번에 더할 수 있는 최대값 k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

result = 0

while True:
  for i in range(k): # 가장 큰 수를 k번 더하기
    if m == 0: break # m이 0이라면 반복문 탈출
    result += first
    m -= 1 # 더할 때마다 1씩 빼기
  if m == 0: break # m이 0이라면 반복문 탈출
  result += second
  m -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답안 출력
