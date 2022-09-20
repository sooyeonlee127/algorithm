arr = [list(map(int, input().split())) for _ in range(4)]
used = [[0] * 4 for _ in range(4)]
def bfs(y, x):
    global used
    cnt = 0
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    q.append([y,x])
    used[y][x] = 1
    cnt += 1
    while q:
        now = q.pop(0)
        yy, xx = now[0], now[1]
        for i in range(4):
            dy = directy[i] + yy
            dx = directx[i] + xx
            if dy < 0 or dx < 0 or dy >= 4 or dx >= 4: continue
            if used[dy][dx] == 1: continue
            if arr[dy][dx] == 0: continue
            q.append([dy, dx])
            used[dy][dx] = 1
            cnt += 1
    return cnt



lst = []
for i in range(4):
    for j in range(4):
        if arr[i][j] == 1 and used[i][j] == 0:
            lst.append(bfs(i, j))

print(max(lst))