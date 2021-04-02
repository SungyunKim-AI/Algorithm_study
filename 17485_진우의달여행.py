"""
백준 17485번 진우의 달 여행
"""

[N, M] = list(map(int, input().split()))
mMap = [[0 for row in range(M+2)] for col in range(N+2)]     # input matrix
# Input
for i in range(1, N+1):
    mMap[i][1:M+1] = list(map(int, input().split()))

# DP : 메모이제이션
# 1. dp[dir][row][col] -> dir : 0(왼쪽 위에서), 1(바로 위에서 오는거), 2(오른쪽 위에서 오는거)
# 2. row = 0 일 때, 초기값 넣어 놓기
# 3. dp[0][row][col] = min(dp[1][row-1][col-1], dp[2][row-1][col-1]) + mMap[row][col]
#    dp[1][row][col] = min(dp[0][row-1][col], dp[2][row-1][col]) + mMap[row][col]
#    dp[2][row][col] = min(dp[0][row-1][col+1], dp[1][row-1][col+1]) + mMap[row][col]
# 4. (dir == 0 and col == 1) or (dir == 1 and col == M) 이면 제거


dp = [[[101 for dir in range(M+2)] for row in range(N+2)] for col in range(3)]
for i in range(3):
    dp[i][1][:] = mMap[1][:]


for row in range(2, N+1):
    for col in range(1, M+1):

        # 맨 왼쪽인데 왼쪽 위에서 오는거 제거
        if dir == 0 and col == 1:
            dp[1][row][col] = min(dp[0][row-1][col], dp[2][row-1][col]) + mMap[row][col]
            dp[2][row][col] = min(dp[0][row-1][col+1], dp[1][row-1][col+1]) + mMap[row][col]

        # 맨 오른쪽인데 오른쪽 위에서 오는거 제거
        elif dir == 1 and col == M:
            dp[0][row][col] = min(dp[1][row-1][col-1], dp[2][row-1][col-1]) + mMap[row][col]
            dp[1][row][col] = min(dp[0][row-1][col], dp[2][row-1][col]) + mMap[row][col]
        else:
            dp[0][row][col] = min(dp[1][row-1][col-1], dp[2][row-1][col-1]) + mMap[row][col]
            dp[1][row][col] = min(dp[0][row-1][col], dp[2][row-1][col]) + mMap[row][col]
            dp[2][row][col] = min(dp[0][row-1][col+1], dp[1][row-1][col+1]) + mMap[row][col]

result = []
for i in range(3):  
    result.append(min(dp[i][N][:]))
result = min(result)

# Output
print(result)

    
    

