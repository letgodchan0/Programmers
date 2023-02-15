result = []

def check(n, x, y, arr):
    num = arr[x][y]  
    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != arr[i][j]:
                check(n//2, x, y, arr)
                check(n//2, x, y + n//2, arr)
                check(n//2, x + n//2, y, arr)
                check(n//2, x + n//2, y + n//2, arr)
                return
    result.append(num)

def solution(arr):
    n = len(arr) 
    check(n, 0, 0, arr)
    answer = [0, 0]
    for v in result:
        if v == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer