def solution(begin, end):
    answer = [1] * (end-begin+1)
    idx = 0
    while idx < len(answer):
        if begin == 1:
            answer[idx] = 0
            begin += 1
            idx += 1
            continue
            
        # begin을 제외한 최대 약수 찾아야 함
        for i in range(2, int(begin**0.5)+1):
            if not begin % i:
                val = begin / i
                if val > 10000000:
                    continue
                answer[idx] = begin / i
                break
        idx += 1
        begin += 1
        
        
    return answer