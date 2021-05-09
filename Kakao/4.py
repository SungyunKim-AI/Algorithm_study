import math
from collections import deque

def solution(n, start, end, roads, traps):
    answer = []
    visited = [1 for _ in range(n+1)]
    trap_index = [[] for _ in range(n+1)]
    for trapNode in traps:
        visited[trapNode] = 2
        for i, road in enumerate(roads):
            if road[0] == trapNode or road[1] == trapNode:
                trap_index[trapNode].append(i)
    
    visited[start] -= 1
    queue = deque([(start, 0)])
    while queue:
        now, dist = queue.popleft()
        if now == end:
            answer.append(dist)
        
        if now in traps:
            for i in trap_index[now]:
                temp = roads[i][0]
                roads[i][0] = roads[i][1]
                roads[i][1] = temp
        
        for road in roads:
            if now == road[0] and visited[road[1]] != 0:
                queue.append((road[1], dist + road[2]))
                visited[now] -= 1
                
    return min(answer)

# print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))