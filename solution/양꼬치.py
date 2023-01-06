def solution(n, k):
    service = n // 10
    answer = n * 12000 + k * 2000 - service * 2000
    return answer