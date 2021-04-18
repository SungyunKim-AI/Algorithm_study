"""
백준 14238 출근기록
분류 : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 깊이 우선 탐색

A는 매일 매일 출근할 수 있다. 
B는 출근한 다음날은 반드시 쉬어야 한다. 
C는 출근한 다음날과 다다음날을 반드시 쉬어야 한다. 
따라서, 모든 출근 기록이 올바른 것은 아니다. 예를 들어, B는 출근한 다음날 쉬어야 하기 때문에, "BB"는 절대로 나올 수 없는 출근 기록이다. 

DP[사용한 A의 개수][사용한 B의 개수][사용한 C의 개수][전전날 출근한 사람][전날 출근한 사람] -> 가능 여부 True, False 저장
"""

def DFS(a, b, c, prev2, prev1):
    # 기저 사례1 : a, b, c 개수가 다 차면 return True
    if [a, b, c] == count:
        return True
    
    # dksdflkajs;odifja;lsdjflaks

    # 기저 사례2 : 메모이제이션 True 이면 이미 확인 한 경우의 수 -> return False
    if dp[a][b][c][prev2][prev1] == True:
        return False
    else:
        dp[a][b][c][prev2][prev1] = True

    # A, B, C 하나씩 증가 시키면서 DFS 재귀 호출
    if a < count[A]:
        result[a+b+c] = 'A'
        if DFS(a+1, b, c, prev2=prev1, prev1=A):
            return True
    
    if b < count[B]:
        if prev1 != B:
            result[a+b+c] = 'B'
            if DFS(a, b+1, c, prev2=prev1, prev1=B):
                return True
    
    if c < count[C]:
        if prev1 != C and prev2 != C:
            result[a+b+c] = 'C'
            if DFS(a, b, c+1, prev2=prev1, prev1=C):
                return True
    
    return False


S = list(input())
A, B, C = 0, 1, 2
count = [S.count(worker) for worker in ('A', 'B', 'C')]
dp = [[[[[False for _ in range(3)] 
                for _ in range(3)] 
                for _ in range(count[C]+1)] 
                for _ in range(count[B]+1)] 
                for _ in range(count[A]+1)]

result = ['']*(len(S))
if DFS(0, 0, 0, 0, 0) == True:
    print(''.join(result))
else:
    print(-1)    



# 예제
# CAB -> BCA
# CBB -> BCB
# BB  -> -1
# BBA -> BAB
# BBAACABACABACBABABAABBAACABACABACBABABAABBAACABACA
# AAAAAAAAAAAAAAAAABABCBABCBABCBABCBABCBABCBABCBABCB
# AABACBCAB
# AAABCABCB
# AAAABCBCBBABCBCBCABCB