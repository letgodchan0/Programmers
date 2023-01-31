from collections import deque

def solution(n, roads, sources, destination):
    
    answer = []
    adj = [[] for _ in range(n+1)]
    visited = [-1 for _ in range(n+1)]
    for a,b in roads:
        adj[a].append(b)
        adj[b].append(a)
    
    visited[destination] = 0
    q = deque([destination])
    while q:
        cur_node = q.popleft()
        for next_node in adj[cur_node]:
            if visited[next_node] < 0:
                visited[next_node] = visited[cur_node] + 1
                q.append(next_node)
    
    for s in sources:
        answer.append(visited[s])
    
    return answer