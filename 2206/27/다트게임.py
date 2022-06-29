# 정규표현식을 너무너무 쓰고싶었는데 결국 잘 몰라서 못썼다.

import re
def other_solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)') # 괄호가 []이게 아니네 1
    dart = p.findall(dartResult) # finditer가 아니네 2
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

def try_sol(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : 3}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    answer = sum(dart)
    return answer

print(try_sol('1D2S#10S'))

def my_solution(dartResult):
    n = ''
    score = []
    for x in dartResult:
        if x.isnumeric():
            n += x
        elif x == 'S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif x == 'D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif x == 'T':
            n = int(n)**3
            score.append(n)
            n = ''
        elif x == '*':
            if len(score) > 1:
                score[-2] = score[-2]*2
                score[-1] = score[-1]*2
            else:
                score[-1] = score[-1]*2
        elif x == '#':
            score[-1] = score[-1] * -1
    return sum(score)