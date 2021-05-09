"""
2020 KAKAO BLIND RECRUITMENT 괄호 변환
균형잡인 괄호 문자열 : (' 의 개수와 ')' 의 개수가 같다면
올바른 괄호 문자열 :  균형잡인 괄호 문자열에서 '('와 ')'의 괄호의 짝도 모두 맞을 경우

문자열 w가 "균형잡힌 괄호 문자열" 이라면 다음과 같은 과정을 통해 "올바른 괄호 문자열"로 변환할 수 있습니다.
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""

def solution(p):
    # 1 : 빈 문자열 반환
    if len(p) == 0:
        return p

    # 2 : 두 "균형잡힌 괄호 문자열" u, v로 분리
    [u, v] = splitBalance(p)

    # 3 : 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행
    if checkCorrect(u):
        u += solution(v)
        return u
    # 4 : 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행
    else:
        answer = '(' + solution(v) + ')'
        print(answer)
        answer += reversing(u[1:-1])
        return answer


# "올바른 괄호 문자열"인지 확인 -> 맞으면 return True
def checkCorrect(p):
    sum = 0
    for i in p:
        if i == '(':    sum += 1
        elif i == ')':
            if sum <= 0:    return False
            else:   sum -= 1
    
    return True if sum == 0 else False


# p를 두 "균형잡힌 괄호 문자열" u, v로 분리하여 리턴
def splitBalance(p):
    numL = 0    # "(" 개수
    numR = 0    # ")" 개수
    for i in range(len(p)):
        if p[i] == '(':
            numL += 1
        elif p[i] == ')':
            numR += 1
        
        if numL == numR:
            return [p[0:i+1], p[i+1:]]

# 괄호 뒤집기
def reversing(p):
    temp = list(p)
    for i in range(len(temp)):
        if temp[i] == '(':
            temp[i] = ')'
        elif temp[i] == ')':
            temp[i] = '('
    
    return ''.join(temp)

print(solution("()))((()"))

"""
예제
p	            result
"(()())()"	    "(()())()"
")("	        "()"
"()))((()"	    "()(())()"
"""

