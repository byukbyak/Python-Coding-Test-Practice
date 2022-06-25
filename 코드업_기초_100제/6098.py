# def can_go(start, end, map):
#     arr = [start]
#     while len(arr) != 0:
#         #1. 현재 위치를 확인하고 그 위치를 올라가고 위치 9로 변경
#         now = arr.pop(0)
#         map[now[0]][now[1]] = 9
#         #2.
#         arr = search_and_update(now, map, arr)
#         if end in arr:
#             return True
#     return False

# def search_and_update(now, map, arr):
#     h, w = len(map), len(map[0])
#     x, y = now
#     if map[max(x-1,0)][y] == 0:
#         arr.append([max(x-1,0)][y])
#     if map[x][max(y-1,0)] == 0:
#         arr.append([x][max(y-1,0)])
#     if map[min(x+1,h-1)][y] == 0:
#         arr.append([min(x+1,h-1)][y])
#     if map[x][min(y+1,w-1)] == 0:
#         arr.append([x][min(y+1,w-1)])
#     return arr

# box = [[0] * 10 for _ in range(10)]

# box = []
# for i in range(10):
#     box.append(list(map(int,input().split())))

# x, y = 1, 1
# limit = len(box) - 2

# while box[x][y] != 2:
#     box[x][y] = 9
#     if [x] == limit and [y] == limit:
#         break
#     elif box[x][y] != 1:
#         y += 1
#     else:
#         x += 1
    
# box[x][y] = 9

# for i in range(10):
#     for j in range(10):
#         print(box[i][j], end=' ')
#     print()

# for i in box:
#   print(' '.join(list(map(str, i))))

##############################################

arr = []

for i in range(10):
    arr.append(list(map(int, input().split())))

row, col = 1, 1
limit = len(arr)-2

while arr[row][col] != 2:
  arr[row][col] = 9
  if row == limit and col == limit:
    break
  elif arr[row][col+1] != 1:
    col += 1
  else:
    row += 1
arr[row][col] = 9

for i in arr:
  print(' '.join(list(map(str, i))))

##############################################

arr = []

for i in range(10):
    arr.append(list(map(int,input().split())))

row, col = 1, 1
limit = len(arr)-2

while arr[row][col]