# 1번
def solution(s):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    c_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    answer = []
    temp = ''
    for c in s:
        temp += c
        if temp in numbers:
            answer.append(temp)
            temp = ''
        elif temp in c_numbers:
            idx = c_numbers.index(temp)
            answer.append(numbers[idx])
            temp = ''
        else:
            continue
    
    return int(''.join(answer))


# 2번
