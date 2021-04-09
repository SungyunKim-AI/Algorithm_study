"""
백준 16236 아기상어
분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치 (처음 크기: 2)

1. 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    3-1. 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    3-2. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
"""
from collections import deque

mMap = []                     # 공간
locX, locY = 0, 0
direct = [[-1, 0, 0, 1], [0, -1, 1, 0]] # 방향(상, 좌, 하, 우)

# Input (add boundary -1)
N = int(input())
mMap.append([-1]*(N+2))
for i in range(1, N+1):
    row = list(map(int, input().split()))
    row.insert(0, -1)
    row.extend([-1])
    mMap.append(row)

    if 9 in row:
        y = row.index(9)
        [locX, locY] = i, y
mMap.append([-1]*(N+2))


# 현재 위치로부터 가장 가까운 거리의 물고기 탐색 -> BFS
def traversal(loc, mSize, exp):
    mMap[loc[0]][loc[1]] = 0
    distance = [[-1]*(N+2) for _ in range(N+2)]
    distance[loc[0]][loc[1]] = 0
    
    queue = deque()
    queue.append((loc[0], loc[1]))
    
    eatPoint = []
    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + direct[0][dir]
            ny = y + direct[1][dir]

            # 경계이거나, 물고기가 더 크면 continue
            if mMap[nx][ny] == -1 or mSize < mMap[nx][ny]:
                continue
            
            # 아직 방문하지 않은 곳이면 방문
            if distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append([nx, ny])

                # 먹을 수 있는 물고기라면, 냠냠
                if mMap[nx][ny] > 0 and mSize > mMap[nx][ny]:
                    eatPoint.append([distance[nx][ny], nx, ny])

    # 거리, 위치 순으로 정렬  
    eatPoint.sort(key = lambda x : (x[0], x[1], x[2]))

    if eatPoint:
        exp += 1
        if mSize == exp:
            mSize += 1
            exp = 0

        return eatPoint[0][1], eatPoint[0][2], mSize, exp, eatPoint[0][0]
    else:
        return 0, 0, 0, 0, 0


# Main
result, mSize, exp = 0, 2, 0
while True:
    locX, locY, mSize, exp, mMin = traversal([locX, locY], mSize, exp)
    result += mMin
    if mMin == 0:   break


# Output
print(result)


"""
예제
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

3
0 0 1
0 0 0
0 9 0

3
0 0 0
0 0 0
0 9 0
"""
