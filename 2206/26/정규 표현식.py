"""
정규 표현식 왜 쓰나?
복잡한 문자열의 처리를 간단하게 할 수 있음
다른 언어에서도 동일하게 사용됨

import re

1. 주만번호 뒷자리 가리기
data = '''
park 900908-1049238
kim  800706-2195749
'''
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

문자 클래스 []
ex) [abc]
- [] 사이 문자들과 매치
- "a" 또는 "before"는 정규식과 일치하는 문자가 있으므로 매치
- "dude"는 없음, 매치되지 않음
- 하이픈(-)을 사용하여 From-To로 표현 가능 [a-c], [0-5] = [012345]

Dot(.)
- 줄바꿈 (\n)을 제외한 모든 문자와 매치
- a.b 라면 aab, a0b 는 매치되지만 abc 는 매치되지 않는다

반복 (*)
ex) ca*t
- ct, cat, caaat는 a가 0번 이상 반복되어 매치

반복 (+)
ex) ca+t
- ca는 0번 반복이라서 매치되지 않음
- cat, caaat는 a가 1번 이상 반복되어 매치

반복 ({m, n}, ?)
ex) ca{2}t
- cat는 a가 1번 반복이라서 매치되지 않음
- caat는 a가 2번 반복되어 매치

ex) ca{2, 5}t
- a가 2이상 5이하 일때 매치

ex) ab?c
- ? == {0, 1} 과 같은 표현
- b가 0 혹은 1회 반복되면 매치

import re
pattern = re.compile('ab*')
패턴객체 생성 = re.compile('정규식')

1. Match
2. Search
3. Findall
4. Finditer

"""

# match
import re
p = re.compile('[a-z]+') # + : 한번 이상 반복
# m = p.match('3 python') # 매치 객체, 하나라도 다르면 None
m = p.match('python')
print(m)

print(m.group()) # 매치된 문자열 리턴
print(m.start()) # 매치된 문자열의 시작 위치 리턴
print(m.end()) # 매치된 문자열의 끝 위치 리턴
print(m.span()) # 매치된 문자열의 (시작, 끝) 튜플로 리턴

# p1 = re.compile('a.b', re.DOTALL)
p1 = re.compile('a.b', re.S) # DOTALL = S : \n 이것도 포함시킴
m1 = p1.match('a\nb')
print(m1)

p2 = re.compile('[a-z]', re.I) # I : 대소문자 무시하고 확인
m2 = p2.match('a\nb')
print(m2)

# p3 = re.compile("^python\s\w+") # ^ : 시작, s: 공백, w : 단어, + : 1번이상 반복
p3 = re.compile("^python\s\w+", re.M) # re.M : 멀티라인, ^를 각 라인의 처음으로 인식시킴
data3 = '''python one
life is too short
python two
you need python
python three'''
# print(p3.findall(data3)) # ['python one'], re.M 없을때
print(p3.findall(data3)) # ['python one', 'python two', 'python three']

# $ : 끝

# VERBOSE : 여러줄 정규표현식, 설명 가능

# 백슬래시 문제 \\ : (r'\\sections') r를 붙여주면 '이거'그대로 인식

# 그룹핑(), ()+,  ?P<name> (?P=name) 또는 print("name")으로 부를 수 있음

# or : | 

# \b : 공백

# 전방탐색 : 긍정형 (?=), 검색할 때 포함하되 출력에서는 제거

# 전방탐색 : 부정형 (?!), 아예 제거

# 문자열 바꾸기 sub
p4 = re.compile('(blue|red|white)')
print(p4.sub('color', 'blue socks and red shoes'))

# Greedy vus Non-Greedy
s = '<html><head><title>'
# print(re.match('<.*>', s).group()) # Greedy
print(re.match('<.*?>', s).group()) # Non-Greedy 최소한 반복

"""
s = p.search('3 python') # 서치 객체, 검색해서 알려줌
print(s)

findall = p.findall('life is too short') # list로 리턴
print(findall)

finditer = p.finditer('life is too short') # iteratort 리턴
for r in finditer:
    print(r)

"""


