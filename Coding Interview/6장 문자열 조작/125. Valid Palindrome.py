# 주어진 문자열이 팰린드롬*인지 확인
# 대소문자 구분하지 않고 영문자, 숫자만을 대상으로 한다
# * 팰린드롬 : 앞뒤가 똑같은, '소주 만 병만 주소 같은' 회문


# s = "A man, a plan, a canal: Panama"
s = "race a car"

# 풀이 1. 리스트로 풀기
# string = []
# ret = ''
# for char in s:
#     if char.isalnum(): # 영문, 숫자만 판별
#         string.append(char.lower())
# while len(string) > 1:
#     if string.pop(0) != string.pop():
#         ret = "false"
#     else:
#         ret = "true"
# print(ret)

# 풀이 2. 데크 자료형
# from collections import deque

# def isPalindrome(self, s: str) -> bool:
#     strs = deque()

#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
    
#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
    
#     return True


# 풀이 3. 슬라이싱
import re
def isPalindrome(self, s: str) -> bool:
    s = s.lower()

    # 정규식
    s = re.sub('[^a-z0-9]','',s)
    
    return s == s[::-1]