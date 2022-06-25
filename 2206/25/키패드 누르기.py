def get_distance(keypad, finget_position, next_number):
    
    next_number_position = keypad[next_number]
    distance = abs(finget_position[0] - next_number_position[0]) + abs(finget_position[1] - next_number_position[1])
    print(f"next_number_position : {next_number_position}, distance : {distance}")
    
    return distance
    
def solution(numbers, hand):
    result = ''
    
    # 현재 위치를 파악하기 위한 딕셔너리
    keypad = {
         1 :(0,0), 2 :(0,1), 3 :(0,3),
         4 :(1,0), 5 :(1,1), 6 :(1,2),
         7 :(2,0), 8 :(2,1), 9 :(2,2),
        '*':(3,0), 0 :(3,1),'#':(3,2)
    }
    
    left_finger_numbers = [1, 4, 7]
    right_finger_numbers = [3, 6, 9]
    middle_finger_numbers = [2, 5, 8, 0]
    
    left_finger_position = keypad['*']
    right_finger_position = keypad['#']
    print(f"left_finger_position : {left_finger_position}, right_finger_position : {right_finger_position}")
    
    for number in numbers:
        if number in left_finger_numbers:
            result += 'L'
            left_finger_position = keypad[number]
            print(f"1. result : {result}")
            print(f"1. left_finger_position : {left_finger_position}, right_finger_position : {right_finger_position}")
        elif number in right_finger_numbers:
            result += 'R'
            right_finger_position = keypad[number]
            print(f"2. result : {result}")
            print(f"2. left_finger_position : {left_finger_position}, right_finger_position : {right_finger_position}")
        else:
            left_finger_distance = get_distance(keypad, left_finger_position, number)
            right_finger_distance = get_distance(keypad, right_finger_position, number)

            if left_finger_distance > right_finger_distance:
                result += 'R'
                right_finger_position = keypad[number]
                print(f"3. result : {result}")
                print(f"3. left_finger_position : {left_finger_position}, right_finger_position : {right_finger_position}")
            elif left_finger_distance < right_finger_distance:
                result += 'L'
                right_finger_position = keypad[number]
                print(f"4. result : {result}")
                print(f"4. left_finger_position : {left_finger_position}, right_finger_position : {right_finger_position}")
            elif left_finger_distance == right_finger_distance:
                result += hand[0].upper()
                if hand == 'right':
                    right_finger_position = keypad[number]
                    print(f"5. result : {result}")
                    print(f"5. left_finger_position : {left_finger_position}, right_finger_position : {right_finger_position}")
                elif hand == 'left':
                    left_finger_position = keypad[number]
                    print(f"6. result : {result}")
                    print(f"6. left_finger_position : {left_finger_position}, right_finger_position : {right_finger_position}")
                    
    return result

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))

    # 테스트 1
    # 입력값 〉	[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
    # 기댓값 〉	"LRLLLRLLRRL"
    # 실행 결과 〉	테스트를 통과하였습니다.
    # 테스트 2
    # 입력값 〉	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"
    # 기댓값 〉	"LRLLRRLLLRR"
    # 실행 결과 〉	테스트를 통과하였습니다.
    # 테스트 3
    # 입력값 〉	[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"
    # 기댓값 〉	"LLRLLRLLRL"