def solution(string):
    answer = []
    cnt1, cnt2 = 0, 0
    while string != '1':
        one, zero = 0, 0
        for s in string:
            if s == '1': one += 1
            else: zero += 1

        string = bin(one)[2:]

        cnt2 += zero
        cnt1 += 1
    answer.append(cnt1)
    answer.append(cnt2)
    return answer