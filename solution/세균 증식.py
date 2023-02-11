def solution(n, t):
    answer = n
    while t:
        answer *= 2
        t -= 1
    return answer