from itertools import combinations

Y, X = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(Y)]

# 0: 빈칸 , 1: 벽, 2: 바이러스
virus = []
blank = []
wall = []
for i in range(Y):
    for j in range(X):
        if MAP[i][j] == 2:
            virus.append([i,j])
        elif MAP[i][j] == 0:
            blank.append([i,j])
        else:
            wall.append([i,j])

test = list(combinations(blank, 3))
safe = len(blank)
directy = [-1,1,0,0]
directx = [0,0,-1,1]
MIN = 21e5
result = []

for T in test:
    q = []
    cnt = 0
    used = [[0]*X for _ in range(Y)]
    for vir in virus:
        q = [vir]
        flag = True
        cnt += 1
        while q:
            y,x = q.pop(0)
            if MIN < cnt:
                flag = False
                break
            for i in range(4):
                dy = directy[i] + y
                dx = directx[i] + x
                if dy < 0 or dy >= Y or dx < 0 or dx >= X: continue
                if used[dy][dx] == 1: continue
                if [dy,dx] in T: continue
                if MAP[dy][dx] == 0:
                    used[dy][dx] = 1
                    cnt += 1
                    q.append([dy,dx])
    if flag and MIN > cnt:
        MIN = cnt
        result = T
print(X*Y - len(wall) - 3 - MIN)
