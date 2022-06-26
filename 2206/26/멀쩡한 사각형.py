def solution(w,h):
    answer = 1
    whole = w * h # 전체
    gcd = 0 # 최대 공약수

    for i in range(min(w, h), 0, -1):
        if w % i == 0 and h % i == 0:
            gcd = i
            break

    return whole - ((w + h) - gcd)

# 실패 이유
# 1. 최대공약수의 필요 이유를 몰랐다.