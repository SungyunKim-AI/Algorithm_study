""" 
백준 20292번 : 컨설팅
"""

commands = []
memory = {} # True : 사용 가능 / False : 사용 불가능

# input
while True:
    line = input().split()
    commands.append(line)
    if line[0] == 'EXIT':
        break
    elif line[0] == 'WRITE':
        memory[line[1]] = True
        memory[line[3]] = True
    else:
        memory[line[1]] = True

for i in range(len(commands)):
    command = commands[i]
    # READ with WRITE
    if command[0] == 'WRITE':
        if  memory[command[1]] == True:
            if memory[command[3]] == True:
                memory[command[1]] = False
                memory[command[3]] = False
            elif memory[command[3]] == False:
                commands.insert(i, ['WAIT'])
                i += 1
                for key in memory.keys():
                    memory[key] = True
        
        else:
            commands.insert(i, ['WAIT'])
            i += 1
            for key in memory.keys():
                memory[key] = True
    
    elif command[0] == 'READ':
        if memory[command[1]] == True:
            memory[command[1]] = False
        else:
            commands.insert(i, ['WAIT'])
            i += 1
            for key in memory.keys():
                memory[key] = True


for command in commands:
    print(' '.join(command))
    