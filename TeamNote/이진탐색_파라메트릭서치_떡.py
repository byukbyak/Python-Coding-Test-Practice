# 파라메트릭 서치 : 최적화 문제를 결정 문제('예' or '아니오')로 바꾸어 해결하는 기법
# 예시 : 특정 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제 (전화번호부 이름 찾기)

# n, m = 4, 6
# array = [19, 15, 10, 17]

n, m = map(int, input().split())
array = list(map(int, input().split())) # 떡의 개수만큼 높이가 존재

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    print(f"while total : {total}, mid : {mid}")
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
            print(f"if x > mid 에서 total : {total}")
        # 떡의 양이 부족한 경우 덜 자르기 (왼쪽 부분 탐색)
        if total < m:
            end = mid - 1
            print(f"if total < m 에서 end : {end}")
        # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            start = mid + 1
            print(f"else 에서 result : {result}, start : {start}")

# 정답 출력
print(result)

# 뭔가 안맞는 것 같은데 내일 다시 확인해보자.. - 22.06.23.THU AM 03:55