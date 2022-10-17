def solution(order):
    stack, answer, i, numbers = [] , 0, 0, list(range(1, len(order) + 1))
    for num in order:
        if num in stack:
            tmp = stack.pop()
            if tmp == num:answer += 1
            else:break      
        else:
            while True:
                if numbers[i] == num:
                    i += 1
                    break
                stack.append(numbers[i])
                i += 1
            answer += 1
    return answer