def find(num):
    result = set()
    for i in range(1, int(num**0.5)+1):
        if not num % i:
            result.add(i)
            result.add(num//i)
    return len(result)
    

def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        res = find(num)
        if res > limit:
            answer += power
        else:
            answer += res
    
    return answer