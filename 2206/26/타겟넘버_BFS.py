# 나의 풀이
def my_solution(numbers, target):
    answer = 0
    return answer

###########################################################################

# Q. 타겟넘버가 왜 DFS/BFS 그래프 문제일까?
# >> 다음 인덱스가 음수인지 아닌지에 따라 여러 답이 나올 수 있기 때문에 모든 정답을 탐색해야한다.

# deque 를 이용한 BFS 풀이
# >> 어차피 인덱스 값에 따라 다음 원소를 결정해야하기 때문에 DFS 인지 BFS 인지는 중요하지 않은 문제
# >> pop 한 임시값 tmp 가 마지막 원소이고 값이 target과 같다면 answer += 1

###########################################################################

from collections import deque

def solution1(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0]) # numbers[0] : 양수 값, 인덱스
    queue.append([-1*numbers[0],0]) # nnumbers[0] 음수 값, 인덱스
    while queue:
        tmp, idx = queue.popleft() # 맨 왼쪽 값을 꺼내 tmp, idx에 할당한다
        idx += 1 # 인덱스를 1씩 증가시키면서 확인 (for loops 같은 역할)
        if idx < n: # idx가 길이보다 작다면
            queue.append([tmp+numbers[idx], idx]) # 맨 왼쪽 값 + 현재 값, 현재 인덱스
            queue.append([tmp-numbers[idx], idx]) # 맨 왼쪽 값 - 현재 값, 현재 인덱스
        else:
            if tmp == target:
                answer += 1
        print(queue)
    return answer

###########################################################################

def solution2(numbers, target):
    # 전체적으로 노드의 합을 더해주는 리스트
    super = [0]

    for i in numbers:
        sub = []
        for j in super:
            sub.append(j+i)
            sub.append(i-j)
            print(f"sub = {sub}")
        super=sub
    # target을 카운트
    print(super)
    return super.count(target)

###########################################################################

numbers = [4, 1, 2, 1]
target = 4
# res = 2
print(solution2(numbers, target))

###########################################################################
