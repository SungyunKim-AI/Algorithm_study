"""
2020 카카오 인터십 _ 수식 최대화

숫자들과 3가지의 연산문자(+, -, *) 만으로 이루어진 연산 수식이 전달되며, 
참가자의 미션은 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출하는 것입니다.
단, 연산자의 우선순위를 새로 정의할 때, 같은 순위의 연산자는 없어야 합니다.

만약 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출하며 제출한 숫자가 가장 큰 참가자를 우승자로 선정하며, 
우승자가 제출한 숫자를 우승상금으로 지급하게 됩니다.
"""

def solution(expression):
    mOperand, mOperator = [], []      # 피연산자 리스트, 연산자 리스트
    priority_list = [['+', '-', '*'],
                    ['+', '*', '-'],
                    ['-', '+', '*'],
                    ['-', '*', '+'],
                    ['*', '+', '-'],
                    ['*', '-', '+']]

    # Input
    tempStr = ''
    for c in expression:
        if c in ['+', '-', '*']:
            mOperand.append(int(tempStr))
            tempStr = ''
            mOperator.append(c)
        else:
            tempStr += c
    mOperand.append(int(tempStr))

    answer = 0
    for priority in priority_list:
        operand = mOperand.copy()
        operator = mOperator.copy()

        for oper in priority:

            while (oper in operator):
                operIndex = operator.index(oper)
                tempAns = calculator(oper, operand[operIndex], operand[operIndex+1])
                # print(tempAns, operIndex)
                del operator[operIndex]
                del operand[operIndex]
                del operand[operIndex : operIndex+1]
                operand.insert(operIndex, tempAns)
            
            if len(operand) == 1:
                answer = max(answer, abs(operand[0]))
                break
            
    return answer

def calculator(operator, x, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    else:
        return 0


"""
입출력 예시
1. "100-200*300-500+20"	    60420
2. "50*6-3*2"	            300
"""

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))