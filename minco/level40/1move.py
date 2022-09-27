import sys
sys.stdin = open('input.txt', 'r')

def path(sy, sx):
    global p
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    q.append([sy,sx])
    p.append([sy,sx])
    while q:
        now = q.pop(0)
        y, x = now[0], now[1]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dx < 0 or dy < 0 or dx >= 4 or dy >= 4: continue
            if arr[y][x] - MAP[y][x] == arr[dy][dx]:
                p.append([dy, dx])
                q.append([dy, dx])

def bfs(sy,sx):
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    q.append([sy,sx])
    while q:
        now = q.pop(0)
        y, x = now[0], now[1]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dx < 0 or dy < 0 or dx >= 4 or dy >= 4: continue
            if min(arr[dy][dx], MAP[dy][dx] + arr[y][x]) == arr[dy][dx] : continue
            if min(arr[dy][dx], MAP[dy][dx] + arr[y][x]) == MAP[dy][dx] + arr[y][x] :
                arr[dy][dx] = MAP[dy][dx] + arr[y][x]
                q.append([dy,dx])




MAP = [list(map(int, input().split())) for _ in range(4)]
arr = [[21e8]*4 for _ in range(4)]
p = []
arr[0][0] = 0
bfs(0,0)
path(3,3)
for i in range(len(p)-1, -1, -1):
    print(f'{p[i][0]},{p[i][1]}')