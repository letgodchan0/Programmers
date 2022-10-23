def solution(X, Y):
    numbers = []
    for i in range(10):
        a = X.count(str(i))
        b = Y.count(str(i))
        if a and b:
            if a == b:
                for _ in range(a):
                    numbers.append(str(i))
            else:
                for _ in range(min(a,b)):
                    numbers.append(str(i))
            
    numbers.sort(reverse=True)

    if not numbers:
        return "-1"
    
    if numbers[0] == "0":
        return "0"

    return "".join(numbers)