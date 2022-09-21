def bfs(y, x, e):
    used = [[0] * X for _ in range(Y)]
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    used[y][x] = 1
    q.append([y,x, 0])
    while q:
        now = q.pop(0)
        yy, xx, level = now[0], now[1], now[2]
        if MAP[yy][xx] == e:
            return yy, xx,level
        for i in range(4):
            dy = directy[i]+yy
            dx = directx[i]+xx
            if dx < 0 or dy < 0 or dx >= X or dy >= Y: continue
            if MAP[dy][dx] == '#': continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy,dx,level+1])




Y, X = map(int, input().split())
MAP = [list(input()) for _ in range(Y)]
order = ['1', '2', '3', '4']

ret = 0
tmp = bfs(0,0,'1')
ret += tmp[2]
tmp = bfs(tmp[0], tmp[1], '2')
ret += tmp[2]
tmp = bfs(tmp[0], tmp[1], '3')
ret += tmp[2]
tmp = bfs(tmp[0], tmp[1], '4')
ret += tmp[2]

print(f'{ret}회')