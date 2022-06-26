def solution(s):
    answer = 10000
    for slicing in range(1, len(s)//2+2): # 문자열 1인 경우를 포함하기 위해 len(s)//2+2
        res = ''
        cnt = 1
        tmp = s[:slicing] # 문자열 슬라이싱 범위 초기화

        for i in range(slicing, len(s)+slicing, slicing):
            if tmp == s[i:i+slicing]:
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt)+tmp
                tmp = s[i:i+slicing]
                cnt = 1
        answer = min(answer, len(res))
    return answer

# s = "aabbaccc" 
# s = "ababcdcdababcdcd"
# print(solution(s))

"""
깨달은 것

1. 전체 문자열의 범위 절반까지가 최대 압축 길이
2. 문자열이 1인 경우를 고려해야함
3. 슬라이싱과 슬라이싱 범위를 활용한 for문을 이용하는 방법

"""