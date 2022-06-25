import math
from itertools import combinations

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    data = combinations(nums, 3)

    for i in data:
        print(sum(i))
        if is_prime(sum(i)) == True:
            answer += 1

    return answer