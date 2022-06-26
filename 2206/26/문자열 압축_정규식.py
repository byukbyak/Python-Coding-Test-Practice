import re # 정규 표현식

def solution(s):
    answer = [] # 문자열의 길이
    
    for slicing in range(1, len(s)//2 + 1):

        p = f'[a-z]{{{slicing}}}' # {{i}}개씩 나눠준다, 현재 s의 경우 8개의 원소가 있기 때문에 3으로 나누면 aab, bac 이후 글자는 매칭되지 않는다.
        p = re.compile(p)
        print(p.findall(s))
        
        str_zip = '' # 압축 문자열
        str_split = p.findall(s) # 잘려진 문자열
        count = 1

        for i in range(len(str_split)-1):
            if str_split[i] == str_split[i+1]: # 잘려진 문자열의 i, i+1이 같다면 count
                count += 1
            else:
                if count > 1 :
                    str_zip += f'{count}{str_split[i]}'
                    print(f'1. str_zip : {str_zip}')
                    count = 1
                else: # 1 또는 0 이라면
                    str_zip += f'{str_split[i]}'
                    print(f'2. str_zip : {str_zip}')
            if i == len(str_split)-2: # len(str_split)-1 만큼만 순회하고 있기 때문에
                if count > 1:
                    if str_split[i] == str_split[i+1]:
                        str_zip += f'{count}{str_split[i]}'
                        print(f'3. str_zip : {str_zip}')
                else:
                    str_zip += f'{str_split[i]}'
                    print(f'4. str_zip : {str_zip}')
    if len(s) % slicing != 0: # 나누어 떨어지지 않는만큼
        str_zip += s[-len(s) % slicing:] # 마지막까지 슬라이싱해서 붙이기

    print(f'str_split : {str_split}')

    answer.append(len(str_zip))
    return answer

# s = "aabbaccc" # 5개 이상부터는 나머지가 3이 되기 때문에 문자열의 길이 / 2까지만 압축을 시도하는게 좋다.
s = "ababcdcdababcdcd"
print(solution(s))
