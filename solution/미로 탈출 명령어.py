from collections import deque

def solution(n, m, x, y, r, c, k):
    def dist(x, y):
        q = deque([(x,y)])
        visited = [[-1] * m for _ in range(n)]
        visited[x][y] = 0
        while q:
            x, y = q.popleft()
            if x == r-1 and y == c-1:
                return visited[x][y]
            
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] < 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    
    def bfs(x, y):
        q = deque([(x, y, "", 0)])
        res = []
        while q:
            x, y, string, cnt = q.popleft()
            
            if (x,y) == (r-1,c-1) and (k - cnt ) % 2 == 1:
                return []
            
            if (x,y) == (r-1,c-1) and cnt == k:
                res.append(string)
                continue
            
            for dx, dy, dt in [(1,0, 'd'),(0,-1, 'l'),(0,1, 'r'),(-1,0, 'u')]:
                nx, ny = x + dx, y + dy
        
                if 0 <= nx < n and 0 <= ny < m and dist(nx, ny) + cnt + 1 <= k:
                    q.append((nx, ny, string + dt, cnt + 1))
                    break
        return res
    
    result = bfs(x-1,y-1)
    if not result:
        return "impossible"
    result.sort()
    return result[0]