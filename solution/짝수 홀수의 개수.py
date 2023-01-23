def solution(num_list):
    answer = []
    a, b = 0, 0
    for num in num_list:
        if num % 2:
            a += 1
        else:
            b += 1
    answer.append(b)
    answer.append(a)
    return answer