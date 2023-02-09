def solution(string):
    
    def check(string):
        stack = ["botton"]
        
        for s in string:

            if len(stack) == 1:
                stack.append(s)
                continue
            
            head = stack.pop()
            if s == ']':
                if head == '[':
                    continue
                
            elif s == '}':
                if head == '{':
                    continue
            
            elif s == ')':
                if head == '(':
                    continue
            else:
                stack.append(head)
                stack.append(s)
                continue
                
            stack.append(head)
            stack.append(s)
        if len(stack) == 1:
            return True
        else: return False
                

    length, answer = len(string), 0
    # if chekc(string): answer += 1
    for _ in range(length):
        string = string[1:] + string[0]
        # print(string)
        if check(string):
            answer += 1
        
    return answer