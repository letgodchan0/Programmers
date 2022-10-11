import heapq

def solution(n, paths, gates, summits):
    summits.sort()
    conn = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        conn[i].append((j, w))
        conn[j].append((i, w))

    pq, MAX = [], float('inf')
    for gate in gates:
        for i, (next_node, next_node_cost) in enumerate(conn[gate]):
            heapq.heappush(pq, (next_node_cost, next_node))

    min_dis = [MAX for _ in range(n + 1)]
    for gate in gates:
        min_dis[gate] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if min_dis[node] <= cost:
            continue
        min_dis[node] = cost
        if node in summits:
            continue
        for next_node, next_node_cost in conn[node]:
            if min_dis[next_node] <= cost:
                continue
            heapq.heappush(pq, (max(cost, next_node_cost), next_node))

    answer = [0, MAX]
    for summit in summits:
        if min_dis[summit] < answer[1]:
            answer[0], answer[1] = summit, min_dis[summit]
    return answer