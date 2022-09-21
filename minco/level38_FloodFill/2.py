def bfs(y,x):
    global used
    cnt = 1
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    used[y][x] = 1
    q = []
    q.append([y,x])
    while q:
        now = q.pop(0)
        yy, xx = now[0], now[1]
        for i in range(4):
            dy = yy + directy[i]
            dx = xx + directx[i]
            if dy < 0 or dx < 0 or dx >= 9 or dy >= 4: continue
            if used[dy][dx] == 1: continue
            if MAP[dy][dx] != MAP[yy][xx] : continue
            used[dy][dx] = 1
            cnt += 1
            q.append([dy, dx])
    return cnt



MAP = [list(map(int, input().split())) for _ in range(4)]
used = [[0]*9 for _ in range(4)]

MAX = 0
for i in range(4):
    for j in range(9):
        ret = 0
        if used[i][j] == 1: continue
        ret = bfs(i,j)
        if ret > MAX:
            MAX = ret * MAP[i][j]

print(MAX)