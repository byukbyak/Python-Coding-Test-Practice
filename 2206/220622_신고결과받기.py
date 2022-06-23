from collections import defaultdict

def solution(id_list, report, k):
    answer = [] # k번 이상 신고되어 처리 결과 메일을 받은 횟수
    report = list(set(report)) # 중복 제거
    user = defaultdict(set) # 신고한 id 카운트
    cnt = defaultdict(int) # 유저별 신고당한 횟수 카운트

    for data in report:
        # report의 a는 신고자 id, b는 신고당한 id
        a, b = data.split()
        # user별 신고한 아이디 추가
        user[a].add(b)
        # 신고당한 아이디의 횟수 추가
        cnt[b] += 1
        
    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
        
    return answer