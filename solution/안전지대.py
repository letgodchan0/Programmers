def solution(board):
    n = len(board)
    answer, total = 0, n**2
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for di, dj in [(0,0),(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                        answer += 1
                        visited[ni][nj] = 1

    return total - answer