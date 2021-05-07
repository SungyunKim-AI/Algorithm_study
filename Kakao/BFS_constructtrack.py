"""
BFS
2020 카카오 인턴십 _ 경주로 건설

이때, 인접한 두 빈 칸을 상하 또는 좌우로 연결한 경주로를 직선 도로 라고 합니다.
또한 두 직선 도로가 서로 직각으로 만나는 지점을 코너 라고 부릅니다.
건설 비용을 계산해 보니 직선 도로 하나를 만들 때는 100원이 소요되며, 코너를 하나 만들 때는 500원이 추가로 듭니다.
죠르디는 견적서 작성을 위해 경주로를 건설하는 데 필요한 최소 비용을 계산해야 합니다.
"""
import math
from collections import deque


def solution(board):
    # 상, 좌, 하, 우
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    N = len(board)

    def BFS(start):
        mMap = [[math.inf for _ in range(N)] for _ in range(N)]
        queue = deque([start])
        
        mMap[0][0] = 0
        while queue:
            row, col, cost, prevDir = queue.popleft()
            
            for nowDir, (dy, dx) in enumerate(dirs):
                nRow = row + dy
                nCol = col + dx

                n_cost = cost + 600 if nowDir != prevDir else cost + 100

                if 0 <= nRow < N and 0 <= nCol < N and board[nRow][nCol] == 0 and mMap[nRow][nCol] > n_cost:
                    mMap[nRow][nCol] = n_cost
                    queue.append((nRow, nCol, n_cost, nowDir))
        
        return mMap[-1][-1]

    answer = min(BFS((0,0,0,2)), BFS((0,0,0,3)))

    return answer



"""
[[0,0,0],[0,0,0],[0,0,0]]	900
[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	3800
[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	2100
[[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	3200
"""

print(solution([[0,0,0],[0,0,0],[0,0,0]]))