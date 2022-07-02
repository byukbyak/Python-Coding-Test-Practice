# def calc(a, b, cnt):
#     return a + b

# def solve(n, ans):
#     ans = 0
#     cnt = 0
#     new = 0
#     s = str(n)
#     if len(s) == 0: # 길이가 0이라면
#         print(s)
#         return 1
#     else:
#         while 1:
#             a = s[0]
#             b = s[1]
#             print(f"a : {a}, b : {b}")
#             res = calc(a, b, cnt, res = 0)
#             if res == n:
#                 ans = cnt
#                 break
#             else:
                
#     return ans

# print(solve(26))

n = int(input())
num = n
cnt = 0

while 1:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b + 10) + c

    cnt += 1
    if (num == n):
        break

print(cnt)