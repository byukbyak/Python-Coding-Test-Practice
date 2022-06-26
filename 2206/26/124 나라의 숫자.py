def solution(n):
    answer = ""
    
    while n: # n != 0
        if n % 3: # n이 3의 배수가 아니라면
            answer += str(n%3) # 나머지를 문자열로 추가해주고(1의자리가 왼쪽에 쌓임)
            n //= 3 # n은 몫으로 바꿔준다
        else:
            answer += str(4)
            n = n // 3 - 1
    
    return answer[::-1] # 역순부터 구했기때문에 역정렬을 해준다