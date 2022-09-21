import copy

def bfs():
    global used
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    used[0][X-1] = 1
    q.append([0,X-1])
    while q:
        now = q.pop(0)
        yy, xx = now[0], now[1]
        for i in range(4):
            dy = directy[i]+yy
            dx = directx[i]+xx
            if dx < 0 or dy < 0 or dx >= X or dy >= Y: continue
            if used[dy][dx] == 1: continue
            if MAP[dy][dx] == '_': continue
            used[dy][dx] = 1
            q.append([dy,dx])

    used[Y-1][0] = 2
    q.append([Y-1,0])
    while q:
        now = q.pop(0)
        yy, xx = now[0], now[1]
        for i in range(4):
            dy = directy[i]+yy
            dx = directx[i]+xx
            if dx < 0 or dy < 0 or dx >= X or dy >= Y: continue
            if used[dy][dx] == 2: continue
            if MAP[dy][dx] == '_': continue
            used[dy][dx] = 2
            q.append([dy,dx])

def bfs2(y,x):
    global used
    backup = copy.deepcopy(used)
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    q.append([y,x,0])
    while q:
        now = q.pop(0)
        yy, xx, level = now[0], now[1], now[2]
        used[yy][xx] = 3
        for i in range(4):
            dy = directy[i]+yy
            dx = directx[i]+xx
            if dx < 0 or dy < 0 or dx >= X or dy >= Y: continue
            if used[dy][dx] == 2 and MAP[dy][dx] == '#':
                used = backup
                return level
            if used[dy][dx] == 2: continue
            if used[dy][dx] == 3: continue
            used[dy][dx] = 3
            q.append([dy,dx,level+1])






Y, X = 8,9
MAP = [list(input()) for _ in range(Y)]
used = [[0] * X for _ in range(Y)]
ret = 0
bfs()


MIN = 21e8
for i in range(Y):
    for j in range(X):
        if used[i][j] == 1:
            ret = bfs2(i,j)
            if ret < MIN:
                MIN = ret

print(ret-1)