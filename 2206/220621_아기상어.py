# https://github.com/byukbyak/Python-Coding-Test-Practice

# BFS 사용 / queue

# 제출코드
import queue
import copy

def findTopLeft(eatable_queue, n):
    # queue(a, b) 형식으로 값이 들어있음 > 1차원으로 변환시킨 후 정렬 > 다시 2차원으로 변환
    tmp = []
    for x, y in queue:
        tmp.append(x*n + y)
        tmp.sort()
        X = tmp[0] // n #?
        Y = tmp[0] % n #?

def isAvailable(x, y, arr, size, n, history): # 이동이 가능한지 여부
    if 0 <= x < n and 0 <= y < n:
        if history[x][y] != 1: # 이미 이전에 방문한 곳, 다시 돌아올 이유는 없다
            if arr[x][y] <= size: # 크기 비교
                return True
    return False

def calc(n, start, arr, size):
    # while len(queue) != 0: # 보통 이렇게 하는데, length 에 따른 구별이 되지 않기 때문에 넣는 큐와 빼는 큐를 구별하는 방법을 사용한다.
    queue = [start]
    a, b = start
    history = [[0] * n for _ in range(n)]
    history[a][b] = 1 # 방문했던 곳

    for length in range(1, n*n):
        next_queue = []
        eatable_queue = []
        for x, y in queue: # 여기서 빼서 next_queue 에 넣는다
            for p, q in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # 상하좌우
                # sudo : if x+p and y+q is available: # 상어가 이동할 수 있는 거리라면
                if isAvailable(x+p, x+q, arr, size, n, history):
                    next_queue.append((x+p), (y+q))
                    history[x+p][y+q] = 1
                    # sudo : if x+p and y+q is eatable: # 상어가 먹을 수 있다면
                    if 0 < arr[x+p][y+q] < size:
                        eatable_queue.append((x+p), (y+q))
        if len(eatable_queue) != 0: # 먹을 수 있는 물고기의 위치로 이동
            x, y = findTopLeft(eatable_queue, n)
            arr[a][b] = 0 # 물고기를 먹고난 위치 상태 업데이트
            arr[x][y] = 9 # 상어의 위치 업데이트
            return length
        if len(next_queue) == 0:
            return 0, 0, 0
        queue = copy.deepcopy(next_queue) # 현재 위치 초기화

def solve():
    n = int(input()) # 최초 입력값
    arr = [] # n * n 2차원 배열

    for i in range(n): # n 만큼 반복
        line = [int(x) for x in input().split()] # 가로
        for j in range(n):
            if line[j] == 9: # start 위치 찾기
                start = (i, j)
                break
        arr.append(line) # 세로
        
    result = 0
    size = 2 # 상어 크기 (먹은 횟수와 같아지면 +1)
    count = 0 # 먹은 횟수
    while True: 
        ret, a, b = calc(n, start, arr, size) # return 값을 clac()로 계산한다 마지막 위치 정보 return(a, b)
        if ret == 0: # return 값이 0이라면 결과를 출력하고
            print(result)
            return
        count += 1
        if count == size:
            size += 1
            count = 0
        result += ret # return 값이 0이 아니라면 resulft에 누적한다
        start = (a, b)

solve()