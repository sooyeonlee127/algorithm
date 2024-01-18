from itertools import combinations

# S: 학생, T: 선생님, X: 아무것도 없음
STU = []
TEA = []
X = []
N = int(input())
MAP = [list(map(str, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 'S':
            STU.append([i,j])
        elif MAP[i][j] == 'T':
            TEA.append([i,j])
        else:
            X.append([i,j])

def check(y, x, wall):
    global N, MAP
    # 상
    for i in range(y-1,-1,-1):
        if MAP[i][x] == 'T':
            return False
        elif [i,x] in wall:
            break
        
    # 하
    for i in range(y+1, N):
        if MAP[i][x] == 'T':
            return False
        elif [i,x] in wall:
            break
        
    # 좌
    for i in range(x-1, -1, -1):
        if MAP[y][i] == 'T':
            return False
        elif [y,i] in wall:
            break
    # 우    
    for i in range(x+1, N):
        if MAP[y][i] == 'T':
            return False 
        elif [y,i] in wall:
            break
    return True   

lst = list(combinations(X,3))

answer = 'NO'
for wall in lst:
    if answer == 'YES':
        break
    flag = True
    for y,x in STU:
        if not check(y,x,wall):
            flag = False
    if flag:
        answer = "YES"
        break
print(answer)