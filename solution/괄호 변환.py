def solution(string):
    # 올바른 괄호 문자열인지 체크하는 함수
    def correct(string):
        stack = ["head"]
        for s in string:
            if len(stack) == 1:
                stack.append(s)
                continue

            last = stack.pop()

            if s == ')':
                if last == '(':
                    continue
            stack.append(last)
            stack.append(s)

        return True if len(stack) == 1 else False
    
    # 균형잡히 괄호 문자열인지 체크하는 함수
    def balance(string):return True if string.count('(') == string.count(')') else False
    
    # u, v로 분리하는 함수
    def split(string):
        tmp = ''
        for i in range(len(string)):
            tmp += string[i]
            if balance(tmp):
                return tmp, string[i+1:]
    
    def make(string):
        if not string: return ""

        u, v = split(string)
        
        if correct(u):
            return u + make(v)
        else:
            new_u = ''
            for i in range(1, len(u) - 1):
                new_u += '(' if u[i] == ')' else ')'

            return '(' + make(v) + ')' + new_u
        
    if correct(string):return string
    
    return make(string)