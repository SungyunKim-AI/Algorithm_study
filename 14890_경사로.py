"""
백준 14890번 경사로
"""

mMap = []    # input matrix
[N, L] = list(map(int, input().split()))

# Input
for i in range(N):
    inputList = list(map(int, input().split()))
    inputList.insert(0, 0)
    inputList.extend([0])
    mMap.append(inputList)

# 열 방향을 transpose 해서 바로 밑에 추가
transMap = list(map(list, zip(*mMap)))
for i in range(1, N+1):
    transMap[i].insert(0,0)
    transMap[i].extend([0])
mMap.extend(transMap[1:-1][:])

# 0으로 테두리 추가
border = [0 for i in range(N+2)]
mMap.insert(0, border)
mMap.extend([border])


# => main
result = 0
for row in range(1, 2*N+1):
    pathLong, downhill, nextLong, completePath = 1, False, 1, True

    for col in range(2, N+1):
        if downhill == True: 
            if mMap[row][col-1] == mMap[row][col]:
                nextLong += 1
                if (col == N) and (nextLong < L):
                    completePath = False
                    break
                if nextLong == L:
                    downhill, nextLong, pathLong = False, 1, 0
                elif nextLong > L:
                    downhill, nextLong, pathLong = False, 1, 1
            elif ((mMap[row][col] - mMap[row][col-1]) == -1) and (nextLong == L):
                downhill, nextLong, pathLong = False, 1, 0
            else:
                completePath = False
                break
        else:
            if mMap[row][col-1] == mMap[row][col]:
                pathLong += 1   
            # 오르막길
            elif (mMap[row][col] - mMap[row][col-1]) == 1:
                if pathLong >= L:
                    pathLong = 1
                else:
                    completePath = False
                    break
            # 내리막길
            elif (mMap[row][col] - mMap[row][col-1]) == -1:
                pathLong, downhill = 0, True
                if (col == N) and (L > 1):
                    completePath = False
                    break
            else:
                completePath = False
                break

    if completePath == True:
        #print(mMap[row][1:-1])            
        result += 1
            

print(result)
