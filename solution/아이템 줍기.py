from collections import deque
def bfs(arr):
    array = [[1] * 102 for _ in range(102)]
    q = deque([])
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for dx, dy in [(0,-1),(0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102:
                if not arr[nx][ny] and array[nx][ny] == 1:  
                    array[nx][ny] = 0
                    q.append((nx, ny))
                elif arr[nx][ny] and array[nx][ny] == 1:
                    array[nx][ny] = 2
            
    return array
    

def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[0] * 102 for _ in range(102)]
    for lx, ly, rx, ry in rectangle:
        for i in range(101-(ry*2), 102-(ly*2)):
            for j in range(2*lx, (2*rx)+1):
                arr[i][j] += 1

    array = bfs(arr)

    q = deque([])
    q.append((101-characterY*2, 2*characterX, 0))
    visited = [[0] * 102 for _ in range(102)]
    visited[101-characterY*2][2*characterX] = 1
    while q:
        
        x, y, cnt = q.popleft()

        if x == 101 - itemY*2 and y == itemX*2:
            return cnt // 2
        
        for dx, dy in [(0,-1),(0,1), (-1,0), (1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102 and array[nx][ny] == 2 and not visited[nx][ny]:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1
                
    
