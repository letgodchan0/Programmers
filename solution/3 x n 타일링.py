def solution(n):
    if n % 2:
        return 0
    a, b = 1, 1
    for _ in range(0, n+1, 2):
        c = 4*b - a
        a, b = b, c %  1000000007
    
    return a