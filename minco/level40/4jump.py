import sys
sys.stdin = open("input.txt", "r")

def bfs(sy,sx):
    q = []
    directy = [1, 1, 1]
    directx = [-1, 0, 1]
    q.append([sy, sx])
    while q:
        now = q.pop(0)
        y, x = now[0], now[1]
        for i in range(3):
            dy = directy[i] + y
            dx = directx[i] + x
            if dx < 0 or dy < 0 or dx >= 3 or dy >= 7: continue
            if MAP[dy][dx] == 0: continue
            if arr[dy][dx] == max(arr[dy][dx], MAP[dy][dx] + arr[y][x]): continue
            if MAP[dy][dx] + arr[y][x] == max(arr[dy][dx], MAP[dy][dx] + arr[y][x]):
                arr[dy][dx] = max(arr[dy][dx], MAP[dy][dx] + arr[y][x])
                q.append([dy, dx])



MAP = [list(map(int, input().split())) for _ in range(7)]
arr = [[-21e8]*3 for _ in range(7)]
arr[0][0] = 1
bfs(0,0)
print(max(arr[6]))
