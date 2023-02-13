def solution(queue1, queue2):
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    total = sum_q1 + sum_q2
    if total % 2: return -1
    
    queue1 = queue1 + queue2
    queue2 = queue2 + queue1
    idx_q1, idx_q2, answer = 0, 0, 0
    
    while sum_q1 != sum_q2:

        if sum_q1 > sum_q2:
            sum_q1 -= queue1[idx_q1]
            sum_q2 += queue1[idx_q1]
            idx_q1 += 1
        else:
            sum_q2 -= queue2[idx_q2]
            sum_q1 += queue2[idx_q2]
            idx_q2 += 1
            
        answer += 1
        if idx_q1 >= len(queue1) or idx_q2 >= len(queue2):
            break
    
    return answer if sum_q1 == sum_q2 else -1