from collections import deque

def solution(maps):
    
    def find(x,y):
        q = deque([(x, y)])
        visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = 0
        while q:
            x, y = q.popleft()

            if maps[x][y] == 'L':
                return (visited[x][y], x, y)
                
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] < 0 and maps[nx][ny] != 'X':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
        return 0, 0, 0
    
    def bfs(x,y):
        q = deque([(x, y)])
        visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = 0
        while q:
            x, y = q.popleft()
            
            if maps[x][y] == 'E':
                return visited[x][y]
                
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] < 0 and maps[nx][ny] != 'X':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
        return -1
    
    st1, st2 = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                st1, st2 = i, j
                break
    
    cnt, nt1, nt2 = find(st1, st2)

    if not cnt:
        return -1
    else:
        check = bfs(nt1, nt2)
        if check < 0:
            return -1
        else:
            return cnt + check
