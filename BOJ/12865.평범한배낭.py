"""
N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데,
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
배낭에 넣을 수 있는 물건들의 가치의 최댓값을 리턴
"""
# 내가 시도했던 방법


# N, K = map(int, input().split())
# stuff = [[0,0]]
# dic = {}
# for _ in range(n):
#     W, V = map(int, input().split())
#     dic[W] = V

# summ = 0

# for weight, value in dic.items():
#     if dic.get(value) <= k:
#         summ += dic[weight]
#         if summ == k:
#             break

# print(summ)
# # print(n, k ,w, v)

# --------------------------------------------------------------

# N, K = map(int, input().split())

# stuff = [[0,0]]
# bag = [[0]*(K+1) for _ in range(N+1)]

# for _ in range(N):
#     stuff.append(list(map(int, input().split())))

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         W = stuff[i][0]
#         V = stuff[i][1]

#     if j < W:
#         bag[i][j] = bag[i-1][j]
#     else:
#         bag[i][j] = max(bag[i-1][j], bag[i-1][j-W]+V)

# print(bag[N][K])

# 아직 너무 어려운가보다

# --------------------------------------------------------------
