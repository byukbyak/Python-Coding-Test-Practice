def solution(d, budget):
    d.sort() # 오름차순 정렬
    count = 0
    # 총 금액과 총 예산 비교
    if sum(d) <= budget: # 예산 이하라면
        return len(d) #  d 길이만큼 리턴
    else: # 예산 밖이라면
        while sum(d) > budget: # 총 금액이 budget 초과시
            d.pop(0)
            count += 1
        return count

# 실패 분석
# 1. sum(d)를 할때마다 시간복잡도가 증가한다.
# 2. 신청한 부서가 통과할 때 budget이 감소되어야하는걸 간과했다.