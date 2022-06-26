def solution(d, budget):
    d.sort() # 오름차순 정렬
    count = 0
    # 신청 부서 개수만큼 순회
    for i in range(len(d)):
        if d[i] <= budget: # 해당 부서가 예산 이하라면
            count += 1 # 카운트하고
            budget -= d[i] # 예산 빼기
        else: # 초과시
            break # 브레이크
    return count

# 비슷한 다른 방법

def solution(d, budget):
    d.sort()
    cnt = 0
    # if sum(d) == budget :
    #     answer = len(d)
    # elif sum(d) < budget :
    #     for i in d :
    #         budget -= i
    #         cnt += 1
    #         answer = cnt
    # else :
    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    answer = cnt
    return answer

# 깨달은 것
# sum(d)를 for 돌리면 시간복잡도 증가하니까 피하는게 좋다!