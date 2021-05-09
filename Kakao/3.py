from collections import deque

def solution(n, k, cmd):
    queue = deque()
    for mCmd in cmd:
        temp = list(mCmd.split(' '))
        if temp[0] == 'D':
            k += int(temp[1])
        elif temp[0] == 'U':
            k -= int(temp[1])
        elif temp[0] == 'C':
            if k == (n-1):
                k -= 1
                queue.append(k)
            else:
                queue.append(k)
            n -= 1
        elif temp[0] == 'Z':
            idx = queue.pop()
            n += 1
            if idx <= k:
                k += 1
        print(mCmd, k)
            
    answer = ['O' for _ in range(n)]
    while queue:
        idx = queue.pop()
        answer[idx] = 'X'
        
    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
#print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))