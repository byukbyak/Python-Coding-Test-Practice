import re # 정규 표현식

def solution(s):
    answer = 0
    
    for i in range(1, len(s)//2 + 1):
        # 패턴 = f'[a-z]{i}'
        pattern = f'[a-z]{{{i}}}'
        print(f"pattern = {pattern}")
        pattern = re.compile(pattern)
        print(pattern.findall(s))
    
    return answer

s = "aabbaccc" # 5개 이상부터는 나머지가 3이 되기 때문에 문자열의 길이 / 2까지만 압축을 시도하는게 좋다.
print(solution(s))
