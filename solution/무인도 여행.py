from collections import deque
def solution(maps):
    def bfs(x,y):
        q = deque([(x,y)])
        visited[x][y] = 1
        res = 0
        while q:
            x, y = q.popleft()
            res += int(maps[x][y])
            
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        
        return res
    
    answer = []
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer