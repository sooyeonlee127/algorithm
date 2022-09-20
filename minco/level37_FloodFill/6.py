def bfs(y, x):
    used = [[0] * 6 for _ in range(4)]
    cnt = 0
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    q.append([y,x])
    used[y][x] = 1
    while q:
        now = q.pop(0)
        yy, xx = now[0], now[1]
        if arr[yy][xx] == 2:
            cnt += 1
        for i in range(4):
            dy = directy[i] + yy
            dx = directx[i] + xx
            if dy < 0 or dx < 0 or dy >= 4 or dx >= 6: continue
            if used[dy][dx] == 1: continue
            if arr[dy][dx] == 1: continue
            q.append([dy, dx])
            used[dy][dx] = 1
    return cnt

arr = [list(map(int, input().split())) for _ in range(4)]

print(bfs(0,0))