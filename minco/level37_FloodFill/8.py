def bfs(y, x):
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
            if dy < 0 or dx < 0 or dx >= M or dy >= N: continue
            if used[dy][dx] == 1: continue
            if MAP[dy][dx] == 0 : continue
            used[dy][dx] = 1
            cnt += 1
            q.append([dy, dx])
    return 1





N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
used = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            if used[i][j] == 1: continue
            result += bfs(i,j)
print(result)