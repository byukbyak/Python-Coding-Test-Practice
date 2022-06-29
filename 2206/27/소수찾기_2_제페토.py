import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    test_case = set()
    
    def find_com(com, res):
        if com != "":
            test_case.add(int(com))
        for i in range(len(res)):
            find_com(com + res[i], res[:i] + res[i+1:])
    find_com("", numbers)

    for i in test_case:
        if is_prime(i):answer += 1
    return answer