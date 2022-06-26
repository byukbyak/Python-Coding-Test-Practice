def solution(bridge_length, weight, truck_weights):
    
    answer = 0 # 경과시간
    bridge = [0] * bridge_length # bridge_length 길이의 다리
    
    while bridge: # 다리가 0이 아닌 동안
        answer += 1 # 1초 증가
        bridge.pop(0) # 맨 왼쪽 item 제거
        
        # 만약 대기열이 0이 아니라면
        if truck_weights:
            
            # 총 현재 다리 무게 + 현재 트럭무게가 다리에 수용가능하다면
            if sum(bridge) + truck_weights[0] <= weight:
                # 대기중인 트럭을 빼서
                t = truck_weights.pop(0)
                # 다리 위에 올린다
                bridge.append(t)
                
            # 수용 불가능한 경우
            else:
                # 다리에 0을 추가한다 (제거 했던것 리셋)
                bridge.append(0)

    return answer

bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(bridge_length, weight, truck_weights))

# 입력값 〉	100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# 기댓값 〉	110