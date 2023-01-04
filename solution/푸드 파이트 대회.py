def solution(food):
    answer, result = '', []
    for i in range(1, len(food)):
        value = food[i] // 2
        if value:
            answer += str(i) * value
            result.append(str(i) * value)
    answer += '0'
    res = ''.join(result)[::-1]
    answer += res
    
    return answer