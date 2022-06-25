w, h = map(int, input().split())
n = int(input())

dp = [[0 for j in range(h)] for i in range(w)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0: # 가로
        for j in range(l):
            dp[x-1][y-1] = 1
            y += 1
    else: # 세로
        for j in range(l):
            dp[x-1][y-1] = 1
            x += 1
    l, d, x, y = 0, 0, 0, 0
    
for i in range(w):
    for j in range(h):
        print(dp[i][j], end=' ')
    print()


# w, h = map(int, input().split())
# dp = [[0 for j in range(h)] for i in range(w)]

# dp = []
# for i in range(w):
#     dp.append([])
#     for j in range(h):
#         dp[i].append(0)

# for i in range(w):
#     for j in range(h):
#         print(dp[i][j], end=' ')
#     print()