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
