def bfs(yy, xx, ty, tx):
    global used
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    used = [[0] * 4 for _ in range(4)]
    q.append([yy, xx, 0])
    used[yy][xx] = 1

    while q:
        now = q.pop(0)
        y, x, level = now[0], now[1], now[2]
        if y == ty and x == tx:
            return level

        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dx < 0 or dy >= 4 or dx >= 4: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy, dx, level + 1])



arr = [[0,0,0,0],
       [1,1,0,1],
       [0,0,0,0],
       [1,0,1,0]]
q = []
sty, stx = map(int, input().split())
edy, edx = map(int, input().split())

print(f'{bfs(sty, stx, edy, edx)}회')

