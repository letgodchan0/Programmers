def solution(a, b, n):
    answer = 0
    while n >= a:
        bottle = n // a
        n -= bottle * a
        full = b * bottle
        answer += full
        n += full
    return answer