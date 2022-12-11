def bfs(sy, sx):
    global used, q
    q.append([sy, sx])
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    while q:
        now = q.pop(0)
        y = now[0]
        x = now[1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dy >= H or dx < 0 or dx >= W: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            if arr[dy][dx] == '#':
                q.append([dy,dx])



T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    used = [[0]*W for _ in range(H)]
    q = []
    cnt = 0
    for i in range(H):
        for j in range(W):
            if used[i][j] == 1: continue
            used[i][j] = 1
            if arr[i][j] == '#':
                bfs(i,j)
                cnt += 1

    print(cnt)
