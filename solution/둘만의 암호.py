def solution(string, skip, index):
    check = []
    for i in range(97, 123):
        tmp = chr(i)
        if tmp not in skip:
            check.append(tmp)
    
    check = check + check + check
    answer = ''
    for s in string:
        idx = check.index(s)
        answer += check[idx+index]
    return answer