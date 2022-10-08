def solution(n, wires):
    wires.sort(key = lambda x : (x[0], x[1]))
    answer = 100
    for first, second in wires:
        check1 = set([first])
        check2 = set([second])
        while True:

            for num1, num2 in wires:
                if (num1 in check1 or num2 in check1) and second != num1 and second != num2:
                    check1.add(num1)
                    check1.add(num2)
                elif (num1 in check2 or num2 in check2) and first != num1 and first != num2:
                    check2.add(num1)
                    check2.add(num2)
            if len(check1) + len(check2) == n:
                break

        answer = answer if abs(len(check1) - len(check2)) > answer else abs(len(check1) - len(check2))
    
    return answer