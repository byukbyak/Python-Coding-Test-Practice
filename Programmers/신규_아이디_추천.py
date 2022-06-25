import re

def solution(new_id):
    answer = ''
    
    # 1. 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2. 알파벳소문자,숫자, '-', '_', '.' 제외한 문자 제거
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    # 3. 마침표가 2번 이상 연속될 때 마침표 1번으로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4. 맨 앞 or 맨 끝에 마침표 제거
    answer = answer[1:] if answer[0] == '.' else answer
    # answer = answer.replace('.','') if answer[-1] == '.' and len(answer) > 1 else answer
    # 만약 맨 뒤에 문자열에 '.'가 있거나 문자열의 길이가 0이 아니라면 문자열의 맨 마지막을 빼고 슬라이싱
    answer = answer[:-1] if len(answer) != 0 and answer[-1] == '.' else answer
    # and 는 둘 중 하나만 false 여도 거짓이니까 앞에꺼가 거짓이면 아예 뒤에를 체크를 안한다
    # 에러 날 가능성이 있는것들은 무조건 뒤쪽에 배치 .. ! (다중조건할경우)
    # 반대로 or 도 다중조건을 걸것이라면 무조건 참일 것 같은걸 왼쪽으로 (먼저거치도록) 배치
    
    print(answer)
    
    # if answer
    
    # 5. 빈 문자열이라면 "a"를 대입
    answer = 'a' if answer == '' else answer
    
    # 6. 16자 이상이면 첫 15개만 남기기
    if len(answer) >= 16:
        answer = answer[:15]
        # 6-1. 15자 중 맨 끝에 마침표가 있다면 제거
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7. 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙이기
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))
    
    return answer

################################################################################################

import re

def solution(new_id):
    answer = ''
    
    # 1. 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2. 알파벳소문자,숫자, '-', '_', '.' 제외한 문자 제거
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    # 3. 마침표가 2번 이상 연속될 때 마침표 1번으로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4. 맨 앞 or 맨 끝에 마침표 제거
    answer = answer[1:] if answer[0] == '.' else answer
    answer = answer[:-1] if len(answer) != 0 and answer[-1] == '.' else answer

    # 5. 빈 문자열이라면 "a"를 대입
    answer = 'a' if answer == '' else answer
    
    # 6. 16자 이상이면 첫 15개만 남기기
    if len(answer) >= 16:
        answer = answer[:15]
        # 6-1. 15자 중 맨 끝에 마침표가 있다면 제거
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7. 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙이기
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))
    
    return answer