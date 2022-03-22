def solution(numbers, target):
    answer = 0
    lst = [0]
    for num in numbers:
        tmp = []
        for l in lst:
            tmp.append(l+num)
            tmp.append(l-num)
        lst = tmp
    for l in lst:
        if l == target:
            answer += 1
    return answer