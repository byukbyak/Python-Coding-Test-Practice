def solution(left, right):
    answer = 0
    for i in range(left, right + 1): # left 부터 right+1 까지 순회
        count = 0 # 약수의 개수를 담을 변수
        for j in range(1, i + 1): # 1 부터 i+1까지 약수 구하기
            if i % j == 0: # 나눠지는 수라면 약수
                count += 1 # 개수 증가
                
        if count % 2 == 0: # 총 약수의 개수가 짝수라면
            answer += i # 그 수를 더해주고
        else:
            answer -= i # 홀수라면 빼준다
    return answer

left = 13
right = 17
print(solution(left, right))
# result = 43