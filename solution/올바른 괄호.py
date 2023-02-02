def solution(string):
    answer = True
    stack = ["tmp"]
    if string == ')' or '(' not in string:
        return False
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            last = stack.pop(-1)
            
            if last == '(':
                continue
                
            stack.append(last)
            stack.append(s)
            
    stack.pop(0)
    return True if not stack else False