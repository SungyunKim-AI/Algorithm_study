"""
투 포인터
2020 카카오 인턴십 _ 보석 쇼핑

진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

"""

def solution(gems):
    kindOfGems = len(set(gems))
    N = len(gems)
    if kindOfGems == 1:
        return [1,1]
    elif kindOfGems == N:
        return [1, N]
    
    answer = [0, N-1]
    start, end = 0, 0
    basket = {gems[start]: 1}

    while start <= end and end < N:
        if len(basket) == kindOfGems:
            if (answer[1] - answer[0]) > (end - start):
                answer = [start, end]
                # print(basket, answer)
            
            if basket[gems[start]] == 1:
                del basket[gems[start]]
            else:
                basket[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == N:
                break

            if gems[end] not in basket:
                basket[gems[end]] = 1
            else:
                basket[gems[end]] += 1
    
    return [answer[0] + 1, answer[1] + 1]


"""
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]
["AA", "AB", "AC", "AA", "AC"]	[1, 3]
["XYZ", "XYZ", "XYZ"]	[1, 1]
["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	[1, 5]
"""

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))