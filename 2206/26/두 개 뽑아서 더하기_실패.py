# import itertools

# def solution(numbers):
#     answer = []
    
#     for x in numbers:
#         for y in range(1, len(numbers)-1):
#             tmp = (x + numbers[y])
#             if tmp not in answer:
                
#             answer.append(tmp)

#     return answer

# 실패 요인
# 1. 조합이 아닌 순열을 쓰려고 했다.
# 2. 각 리스트의 아이템마다 sum 한 값만을 answer에 넣고싶었는데 방법만 알고 구현 방법을 몰랐다.
# 3. 더한 값의 총 합이 같을 경우 중복되는 값이 answer 에 있으면 안된다는 것을 간과하고 있었다.
# 4. itertools 사용법 미숙

import itertools

def solution(numbers):
    answer = set()
    
    for i in list(itertools.combinations(numbers, 2)): # 이렇게 하면 한번에 조합 리스트가 만들어진다
        # 각 조합의 합만 넣어준다
        answer.add(sum(i)) # set 이니까 append()가 아닌 add() 사용
    return sorted(answer) # 혹시 모르니까 정렬해서 리턴

numbers = [2,1,3,4,1]
# result = [2,3,4,5,6,7]

print(solution(numbers))