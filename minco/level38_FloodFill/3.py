def bfs(y,x):
    global flag, used
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    used[y][x] = 1
    q.append([y,x, 0])
    while q:
        now = q.pop(0)
        yy, xx, level = now[0], now[1], now[2]
        for i in range(4):
            dy = directy[i]+yy
            dx = directx[i]+xx
            if dx < 0 or dy < 0 or dx >= 7 or dy >= 7: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy,dx,level+1])
            if MAP[dy][dx] == 2:
                if level+1 < 4:
                    flag = 0
                return


def bfs1(y,x):
    global flag, used1
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    used[y][x] = 1
    q.append([y,x, 0])
    while q:
        now = q.pop(0)
        yy, xx, level = now[0], now[1], now[2]
        for i in range(4):
            dy = directy[i]+yy
            dx = directx[i]+xx
            if dx < 0 or dy < 0 or dx >= 7 or dy >= 7: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy,dx,level+1])
            if MAP[dy][dx] == 1:
                if level+1 < 3:
                    flag = 0
                return



MAP = [list(map(int, input())) for _ in range(7)]
flag = 1

used = [[0] * 7 for _ in range(7)]
used1 = [[0] * 7 for _ in range(7)]

for i in range(7):
    for j in range(7):
        if MAP[i][j] == 2:
            if used[i][j] == 1: continue
            bfs(i, j)
        elif MAP[i][j] == 1:
            if used1[i][j] == 1: continue
            bfs1(i,j)

if flag:
    print('pass')
else:
    print('fail')