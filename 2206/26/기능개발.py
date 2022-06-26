# from collections import deque

# def solution(progresses, speeds):
#     answer = []
#     q = deque(100 - x for x in progresses)
#     print(f"[ 최초 잔여 : {q} ]")
#     count = 0
#     days = 0
    
#     while len(q) == 0:
#         for i in range(len(speeds)):
#             if q[i] <= 100:
#                 q[i] += speeds[i]
#                 days += 1
#                 print(f"[ 배포가능일 : {days} ]")
#             else:
#                 q.pop(0)
#                 break
#     return answer

# 실패 분석
# queue 를 잘 모른다

import math

def solution(progresses, speeds):
    answer = []
    front = 0 # 맨 왼쪽 값 체크 변수
    # progresses, speeds를 병렬처리한 후 잔여일수를 계산해서 리스트를 초기화
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    
    for idx in range(len(progresses)): # progresses의 길이만큼 순회
        if progresses[idx] > progresses[front]: # 만약 현재 인덱스 값이 front 값보다 크다면
            answer.append(idx - front) # 현재 인덱스 - front 값 (한번에 처리되는 데이터의 양)을 answer에 넣어준다.
            front = idx # front 인덱스 값 0 에서 현재 인덱스로 초기화
    answer.append(len(progresses) - front) # 맨 마지막 인덱스는 for 문을 돌지 않기 때문에 전체 길이에서 front 값을 빼준다.
    
    return answer

# 배운것
# math.ceil은 소수점 올림, floor 내림, round는 반올림
# zip 함수 쓰는 법

# 다시 작성

import math

def solution(progresses, speeds):
    answer = []
    # 1. 잔여일수로 데이터 초기화
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    # 2. front 체크
    front = 0
    # 3. 맨 왼쪽부터 체크
    for i in range(len(progresses)):
        # 4. 현재 인덱스 값이 front 보다 크다면
        if progresses[i] > progresses[front]:
            # 5. answer 에 (현재 인덱스 - 맨 앞 인덱스)
            answer.append(i - front)
            # 6. front 값 현재로 초기화
            front = i
    # 7. 맨 마지막까지 확인 (전체 길이 - 현재 인덱스)
    answer.append(len(progresses) - front)

    return answer

# queue 를 활용한 다른 답변
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer