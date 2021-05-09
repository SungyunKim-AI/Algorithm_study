"""
순열 조합
2019 카카오 개발자 인턴 _ 불량 사용자

제재 아이디 : 불량 사용자 목록에 매핑된 응모자 아이디
이벤트 응모자 아이디 목록이 담긴 배열 user_id와 불량 사용자 아이디 목록이 담긴 배열 banned_id가 매개변수로 주어질 때, 
당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지 return 하도록 solution 함수를 완성해주세요.
"""
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    for com_set in permutations(user_id, len(banned_id)):
        if mapping_check(com_set, banned_id):
            com_set = list(com_set)
            com_set.sort()  # answer 리스트 안에서 비교할 수 있도록 정렬
            # print(com_set)
            if com_set not in answer:
                answer.append(com_set)

    return len(answer)

def mapping_check(com_set, banned_id):
    for i in range(len(com_set)):
        if len(com_set[i]) == len(banned_id[i]):
            for j in range(len(com_set[i])):
                if com_set[i][j] == banned_id[i][j] or banned_id[i][j] == '*':
                    continue
                else:
                    return False
        else:
            return False
    return True
    




"""
["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "abc1**"]	2
["frodo", "fradi", "crodo", "abc123", "frodoc"]	["*rodo", "*rodo", "******"]	2
["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "*rodo", "******", "******"]	3
"""

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))