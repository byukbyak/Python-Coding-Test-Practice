def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        if signs[i] != True:
            answer.append(absolutes[i]*-1)
        else:
            answer.append(absolutes[i])
    return sum(answer)