def solution(array, commands):
    answer = []

    # 1. commands에 있는 i,j,k를 뽑는다 -> i=x[0], j=x[1], k=[2]
    for command in commands:
        i, j, k = command[0], command[1], command[2]
    # 2. i-1, j 부터 slice 한다.
        slice = array[i-1:j]
    # 3. sort() 이용하여 list를 정렬한다.
        slice.sort()
    # 4. k번째에 있는 수를 indexing
        answer.append(slice[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
# return = [5, 6, 3]