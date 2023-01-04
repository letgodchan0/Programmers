def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for i in range(m-1, len(score), m):
        if i < len(score):
            answer += score[i] * m
    return answer