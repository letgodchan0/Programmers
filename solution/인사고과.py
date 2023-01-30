def solution(scores):
    check, answer, wanho = 0, 1, scores[0]
    scores.sort(key=lambda x : (-x[0], x[1]))
    
    for a, b in scores:
        if wanho[0] < a and wanho[1] < b:
            return -1
        if check <= b:
            if a + b > sum(wanho):
                answer += 1
            check = b
    
    return answer