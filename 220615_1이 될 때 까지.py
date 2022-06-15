# 내가 푼 답안
n, k = map(int, input().split())
result = 0

while True:
  if n == 1: break
  elif n % k == 0:
    n = n // k
    result += 1
  else:
    n = n - 1
    result += 1
    
print(result)

###################################

# 답안 예시
n, k = map(int, input().split())
result = 0

while True:
  # (n == k로 나누어떨어지는 수)가 될때까지 1씩 빼기
  targer = (n//k) * k
  result += (n - target)
  n = target
  # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k: break
  # k로 나누기
  result += 1
  n //= k
  
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
