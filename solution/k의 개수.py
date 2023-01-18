def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        check = list(str(num))
        answer += check.count(str(k))
    
    return answer