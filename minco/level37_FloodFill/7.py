def bfs(y1,x1,y2,x2):
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    used = [[0]*M for _ in range(N)]
    level = 0
    q = []
    q.append([y1,x1,level])
    used[y1][x1] = 1

    while q:
        now = q.pop(0)
        y, x, level = now[0], now[1], now[2]
        if y == y2 and x == x2:
            return level
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dx < 0 or dx >= M or dy >= N: continue
            if used[dy][dx] == 1: continue
            if MAP[dy][dx] == 'x': continue
            used[dy][dx] = 1
            q.append([dy, dx, level+1])


N, M = map(int, input().split())
MAP = [list(input().split()) for _ in range(N)]


for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'S':
            sty, stx = i, j
        if MAP[i][j] == 'C':
            my, mx = i, j
        if MAP[i][j] == 'D':
            edy, edx = i, j


ret = bfs(sty, stx, my, mx) + bfs(my, mx, edy, edx)
print(ret)