"""
2020 카카오 인턴십_키패드 누르기

1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
    4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
"""


def solution(numbers, hand):
    answer = ''
    nowL, nowR = -11, -22;
    keyPad = {1: (0,0), 2: (0,1), 3: (0,2),
                4: (1,0), 5: (1,1), 6: (1,2),
                7: (2,0), 8: (2,1), 9: (2,2),
                -11: (3,0), 0: (3,1), -22: (3,2)}
    
    for number in numbers:
        LR_flag = ''      # L -> Left, R -> Right
        
        if number in [1,4,7]:
            LR_flag = 'L'
        elif number in [3,6,9]:
            LR_flag = 'R'
        else:
            # Left, Rigth 거리 계산
            distanceL = abs(keyPad[nowL][0] - keyPad[number][0]) + abs(keyPad[nowL][1] - keyPad[number][1])
            distanceR = abs(keyPad[nowR][0] - keyPad[number][0]) + abs(keyPad[nowR][1] - keyPad[number][1])
            
            if distanceL > distanceR:
                LR_flag = 'R'
            elif distanceL < distanceR:
                LR_flag = 'L'
            else:
                if hand == "right":
                    LR_flag = 'R'
                else:
                    LR_flag = 'L'
        
        if LR_flag == 'L':
            nowL = number
        elif LR_flag == 'R':
            nowR = number
        answer += LR_flag
                      
    return answer




"""
입출력 예시
1. [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	    "LRLLLRLLRRL"
2. [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	    "LRLLRRLLLRR"
3. [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	    "right"	    "LLRLLRLLRL"
"""

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))