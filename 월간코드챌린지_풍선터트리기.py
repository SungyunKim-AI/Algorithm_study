"""
프로그래머스 월간 코드 챌린지 시즌1 풍선 터트리기
"""

def solution(a):
    # 어떤 수를 기준으로 왼쪽, 오른쪽으로 나누었을 때 그 수가 가장 작으면 최후까지 남길 수 있다.
    result = [False for i in range(len(a))]
    minLeft, minRight = 1000000001, 1000000001
    for i in range(len(a)):
        if a[i] < minLeft:
            minLeft = a[i]
            result[i] = True
        
        if a[-(1+i)] < minRight:
            minRight = a[-(1+i)]
            result[-(1+i)] = True
    
    return sum(result)



print(solution([9,-1,-5]))                              # result = 3
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))  # result = 6
print(solution([1,2,3,4,5,6,7,8,9,10]))
