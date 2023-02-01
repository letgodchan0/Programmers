def solution(n):  
    a, b= 0, 1
    for i in range(n):
        a, b = b, (a+b) % 1000000007
    
    return b