import sys
n = int(sys.stdin.readline())
for i in range(n, 0, -1):
    print(i)

# 시간 초과
# def back(n):
#     if n != 1:
#         print(n)
#         return back(n - 1)
#     elif n == 1:
#         return 1

# print(back(n))