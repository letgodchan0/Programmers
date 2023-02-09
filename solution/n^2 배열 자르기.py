def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        x, y = divmod(i, n)
        x += 1
        y += 1

        if y < x:
            answer.append(x)
        else:
            # x가 x개 있음, 223 y가 이라면 n=3, x=2, y=2            
            answer.append(y)

    return answer