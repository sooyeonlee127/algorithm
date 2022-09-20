arr = [list(map(int, input().split())) for _ in range(4)]
q = []
used = [[0]*5 for _ in range(4)]

for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            q.append([i, j, 0])
            used[i][j] = 1

directy = [-1, -1, -1, 0, 0, 1, 1, 1]
directx = [-1, 0,1 , -1, 1, -1, 0, 1]


while q:
    now = q.pop(0)
    y, x, level = now[0], now[1], now[2]
    arr[y][x] = level
    for i in range(8):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy < 0 or dx < 0 or dy >= 4 or dx >= 5: continue
        if used[dy][dx] == 1: continue
        used[dy][dx] = 1
        q.append([dy, dx, level+1])

MAX = 0
for i in range(4):
    for j in range(5):
        if MAX < arr[i][j]:
            MAX = arr[i][j]

print(MAX)