def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

left = 13
right = 17
print(solution(left, right))
# result = 43

# << 해석 >>
# i**0.5 는 제곱근을 구하는 식 (4의 제곱근은 2, 25의 제곱근은 5)
# 제곱근이 정수로 표현 가능한 수는 나누어 떨어지지 않는 경우가 있다
# 예를 들어 10 의 제곱근은 3.162277 .. 하지만 약수의 개수는 4
# 따라서 int를 씌웠을때와 씌우지 않았을 때 값이 같지 않다면
# 그 수는 약수의 개수가 짝수라는 뜻이고 같다면 홀수라는 뜻이 된다