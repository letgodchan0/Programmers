def solution(k, score):
    answer, result = [], []
    for s in score:
        answer.append(s)
        if len(answer) < k:
            result.append(min(answer))
        else:
            answer.sort(reverse=True)
            result.append(min(answer[:k]))
    return result