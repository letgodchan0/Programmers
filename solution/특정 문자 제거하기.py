def solution(my_string, letter):
    answer = ''
    for my in my_string:
        if my != letter:
            answer += my
    return answer