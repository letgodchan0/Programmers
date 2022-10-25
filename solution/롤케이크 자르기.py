def solution(topping):
    answer, check = -1, {}

    for t in topping:
        check[t] = check.get(t, 0) + 1
    
    tmp, length = set(), len(check)
    
    for t in topping:
        check[t] -= 1
        if check[t] == 0:
            length -= 1
        tmp.add(t)
        if length == len(tmp):
            answer += 1    
        
    return 0 if answer == -1 else answer + 1