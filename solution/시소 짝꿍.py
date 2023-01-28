from collections import Counter
def solution(weights):
    weights.sort()
    counter = Counter(weights)
    answer = 0
    
    for key, value in counter.items():
        if counter.get(key) > 1:
            answer += value*(value-1) // 2
    
    for w in set(weights):
        for k in (2/3, 3/4, 1/2):
            if counter.get(w * k):
                answer += counter.get(w) * counter.get(w*k)
    
    return answer