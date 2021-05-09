# distance = |r1 - r2| + |c1 - c2| > 2

dirs = [(-2,0), (-1,-1), (-1, 0), (-1, 1),
       (0,-2), (0,-1), (0,1), (0, 2),
       (1,-1), (1,0), (1,1), (2,0)]
    
def solution(places):
    answer = []
    for i, mMap in enumerate(places):
        print(i)
        flag = True
        for row in range(5):
            for col in range(5):
                if mMap[row][col] == 'P':
                    print(row, col)
                    if dist_check(mMap, row, col):
                        continue
                    else:
                        flag = False
                        break
            if flag == False:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer

def dist_check(mMap, row, col):
    for (y, x) in dirs:
        nRow = row + y
        nCol = col + x
        
        if nRow < 0 or nRow >= 5 or nCol < 0 or nCol >= 5:
            continue
            
        if mMap[nRow][nCol] == 'P':
            if (y,x) in [(-1,0),(0,-1),(0,1),(1,0)]:
                print(nRow, nCol)
                return False
            elif (y,x) in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                if mMap[nRow-y][nCol] != 'X' or mMap[nRow][nCol-x] != 'X':
                    print(nRow, nCol)
                    return False
            else:
                if (y,x) == (-2,0) and mMap[nRow+1][nCol] != 'X':
                    print(nRow, nCol)
                    return False
                elif (y,x) == (2,0) and mMap[nRow-1][nCol] != 'X':
                    print(nRow, nCol)
                    return False
                elif (y,x) == (0,2) and mMap[nRow][nCol-1] != 'X':
                    print(nRow, nCol)
                    return False
                elif (y,x) == (0,-2) and mMap[nRow][nCol+1] != 'X':
                    print(nRow, nCol)
                    return False
                else:
                    continue
    return True


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))