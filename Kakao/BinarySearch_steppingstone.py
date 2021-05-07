"""
이진 탐색
2019 카카오 개발자 겨울 인턴 _ 징검다리 건너기

- 징검다리는 일렬로 놓여 있고 각 징검다리의 디딤돌에는 모두 숫자가 적혀 있으며 디딤돌의 숫자는 한 번 밟을 때마다 1씩 줄어듭니다.
- 디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며 이때는 그 다음 디딤돌로 한번에 여러 칸을 건너 뛸 수 있습니다.
- 단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있습니다.
"""

# 정확도 코드
# def solution(stones, k):
#     answer = 200000001 
#     for i in range(len(stones)-k+1):
#         maxVal = max(stones[i : i+k])
#         answer = min(maxVal, answer)

#     return answer

# 효율성 코드
def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2

        count = 0
        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
            if count == k:
                break

        if count >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))      # 정답 : 3