def solution(s):
    answer = s
    nums = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    # dict.items() 함수는 각 아이템을 전부 불러오며 [0]은 key 값을, [1]은 value 값을 가지고 온다
    for item in nums.items():
        # replace(1, 2) 는 string의 1을 2로 치환해준다
        answer = answer.replace(item[0], str(item[1]))
    
    return int(answer)