from itertools import combinations

def solution(numbers):
    answer = set() # 중복을 제거하기 위해 set으로 선언해준다
    
    for i in list(combinations(numbers, 2)): # 2개로 이루어진 모든 조합을 뽑는다
        answer.add(sum(i)) # 하나의 i 안에 있는 조합의 합을 더한다
        
    return sorted(answer) # 정렬해서 리턴