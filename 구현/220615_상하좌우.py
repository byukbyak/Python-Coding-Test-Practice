# 구현, 시뮬레이션

n = int(input()) # map size
plans = input().split()
move_types = ['L', 'R', 'U', 'D']
here = [1, 1] # start point
map = []

for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        map.append([i],[j])
        print(map)

