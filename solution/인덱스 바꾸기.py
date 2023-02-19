def solution(my_string, num1, num2):
    result = list(my_string)
    result[num1], result[num2] = result[num2], result[num1]
        
    return "".join(result)