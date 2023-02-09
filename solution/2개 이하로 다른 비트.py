def solution(numbers):
    answer = []
    for num in numbers:
        if num % 4 == 3:
            Temp = '0' + bin(num)[2:]
            for i in range(len(Temp)-1, -1, -1):
                if Temp[i] == '0':
                    answer.append(int(Temp[0:i] + "10" + Temp[i+2:],2))
                    break
        else:
            answer.append(num+1)
    return answer