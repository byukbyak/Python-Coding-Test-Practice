n = int(input())
a = list(map(int, input().split()))
dp = [0] * (23 + 1)

for x in a:
    dp[x] += 1
result = dp[1:]
print(" ".join(map(str, result)))