def solution(msg):
    check, idx, answer = {}, 1, []
    idx = 1
    for i in range(65, 91):
        check[chr(i)] = idx
        idx += 1
    
    if len(msg) == 1:
        return [check.get(msg)]
    
    i = 0
    while i < len(msg):
        string, k = msg[i], 1
        while i+k < len(msg):
            new_string = string + msg[i+k]
            if not check.get(new_string):
                break
                 
            string += msg[i+k]
            k += 1

        answer.append(check.get(string))
        check[new_string] = max(check.values()) + 1
        i += k
    
    return answer