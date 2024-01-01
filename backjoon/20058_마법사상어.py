"""
그래프 이론, 그래프 탐색, 시뮬레이션
백준 20058_마법사 상어와 파이어 스톰

행렬 크기 : 2^N
파이어스톱 시전 횟수 : Q
"""

def stage(A, N, L):
    rotateA = [[0 for _ in range(N)] for _ in range(N)]
    L = 2 ** L
    for i in range(N):
        cntRow = (i//L) * L
        for j in range(N):
            cntCol = (j//L) * L
            if i%2 == 0 and j%2 == 0:
                rotateA[cntRow][cntCol+1] = A[i][j]
            elif i%2 == 0 and j%2 == 1:
                rotateA[cntRow+1][cntCol+1] = A[i][j]
            elif i%2 == 1 and j%2 == 0:
                rotateA[cntRow][cntCol] = A[i][j]
            elif i%2 == 1 and j%2 == 1:
                rotateA[cntRow+1][cntCol] = A[i][j]

    return rotateA


if __name__ == "__main__":
    A = []
    N, Q = list(map(int, input().split()))
    N = 2 ** N
    for i in range(N):
        row = list(map(int, input().split()))
        A.append(row)
    L = list(map(int, input().split()))

    rotateA = stage(A, N, 2)
    print(rotateA)



"""
3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1

3 1
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
1
"""

