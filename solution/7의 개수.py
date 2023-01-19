def solution(array):
    answer = 0
    for a in array:
        answer += list(str(a)).count('7')
    return answer