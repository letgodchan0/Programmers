def solution(want, number, discount):
    answer = 0
    result = {}
    for i in range(len(want)):
        result[want[i]] = number[i]
        
    for i in range(len(discount)-9):
        check = {}
        for k in discount[i:i+10]:
            check[k] = check.get(k, 0) + 1

        for w in want:
            if w not in check.keys() or result[w] != check.get(w):
                break
        else:
            answer += 1
                
    return answer