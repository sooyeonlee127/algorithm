N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
starty, startx = map(int, input().split())
level = 0
q = []

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]


used = [[0]*M for _ in range(N)]
q.append([starty, startx, level])
used[starty][startx] = 1

while q:
    now = q.pop(0)
    y, x, level = now[0], now[1], now[2]
    arr[y][x] = level
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy < 0 or dx <0 or dy >= N or dx >= N: continue
        if used[dy][dx] == 1: continue
        if arr[dy][dx] == 0:
            used[dy][dx] = 1
            q.append([dy, dx, level+1])


MAX = 0
for i in range(N):
    for j in range(N):
        if MAX < arr[i][j]:
            MAX = arr[i][j]
print(MAX)