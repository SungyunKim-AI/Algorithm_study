""" 
백준 20292번 : 컨설팅

메모리는 3가지 상태가 있을 수 있다.
-> READ or WORKING or READY
WRITE A TO B : A(READ) && B(WORKING)
"""

commands = []
memory = {} # True : 사용 가능 / False : 사용 불가능

def WAIT_operator():
    commands.insert(-1, ['WAIT'])
    memory.clear()


while True:
    # 입력
    command = input().split()
    commands.append(command)

    # EXIT 종료
    if command[0] == 'EXIT':
        break

    # WIRTE
    elif command[0] == 'WRITE':
        # Memory에 없으면 추가
        if command[1] not in memory:
            memory[command[1]] = 'READY'
        if command[3] not in memory:
            memory[command[3]] = 'READY'

        # Operation 검사
        if memory[command[1]] == 'WORKING' or memory[command[3]] != 'READY':
            WAIT_operator()
        
        memory[command[1]] = 'READ'
        memory[command[3]] = 'WORKING'
    
    # READ
    elif command[0] == 'READ':
        # Memory에 없으면 추가
        if command[1] not in memory:
            memory[command[1]] = 'READY'

        # Operation 검사
        if memory[command[1]] == 'WORKING':
            WAIT_operator()
        
        memory[command[1]] = 'READ'
    


# 출력
for command in commands:
    print(' '.join(command))
    