def solution(my_string, n):
    answer = ''
    for string in my_string:
        answer += string * n
    return answer