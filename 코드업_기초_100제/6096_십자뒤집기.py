dp = []

for i in range(19):
    dp.append([])
    new_line = list(map(int, input().split()))
    for j in range(19):
        # print(, end=" ")
        dp[i].append(new_line[j])
    new_line = []
    # print(" ".join(map(str, dp[i])))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if dp[j][y-1] == 0:
            dp[j][y-1] = 1
        else:
            dp[j][y-1] = 0
        if dp[x-1][j] == 0:
            dp[x-1][j] = 1
        else:
            dp[x-1][j] = 0

for i in range(19):
    for j in range(19):
        print(dp[i][j], end=" ")
    print()