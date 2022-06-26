def solution(n, lost, reserve):
    stack = []
    
    # 중복 제거
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    # 여유 있는 학생 번호 확인
    for x in set_reserve:
        # 왼쪽 먼저 확인
        if (x-1) in set_lost:
            set_lost.remove(x-1)
        # 오른쪽 확인
        elif (x+1) in set_lost:
            set_lost.remove(x+1)

    return n - len(set_lost)