from collections import deque
def solution(x, y, n):
    def bfs():
        q = deque([(y, 0)])
        cnt = 0
        while q:
            num, cnt = q.popleft()
            if num == x:
                return cnt
            
            new = num - n
            if new >= x:
                q.append((new, cnt + 1))
            
            if not num % 2:
                new = num // 2
                if new >= x:
                    q.append((new, cnt + 1))
            
            if not num % 3:
                new = num // 3
                if new >= x:
                    q.append((new, cnt + 1))
                
        return -1
    
    answer = bfs()
    return answer