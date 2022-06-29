# import itertools
# import math

# def is_prime(n):    
#     for i in range(2, int(math.sqrt(n))+1): # 제곱근을 정수화 시켜준 후 +1
#         if n % i == 0:
#             return False
#     return True

# def solution(numbers):
#     count = 0
    
#     set_pmt = list(set(list(map(''.join, itertools.permutations(numbers)))))
#     print(set_pmt)
    
#     # 1. 순열이 소수라면 count+1
#     for x in set_pmt:
#         if is_prime(int(x)) == True:
#             count +=1
    
#     # 2. 투 포인터로 확인
#     n_list = list(map(''.join, numbers))
#     print(n_list)
    
#     result = 0
#     summary = False
#     end = 1

#     for start in range(len(n_list)):
#         tmp = n_list[start] + n_list[end]
#         print(tmp)
#         # summary = is_prime(int())
#         while (summary != True) and end < len(n_list):
#             end += 1
#         # 부분 합이 m일 때 카운트 증가
#         if summary == True:
#             result += 1
#         summary = False

#     print(result)
    
#     return count

# 투포인터는 합을 구할 때 쓰이는데
# 이건 조합을 구하는 문제라서 쓰면 안됐던 것 같다
# 이렇게 접근하는 것 보다 슬라이싱을 이용하고 비교를 하는게 맞는 것 같다\


import itertools
import math

def is_prime(n):    
    for i in range(2, int(math.sqrt(n))+1): # 제곱근을 정수화 시켜준 후 +1
        if n % i == 0:
            return False
    return True

def solution(numbers):
    count = 0
    # 1. 각 

    return count