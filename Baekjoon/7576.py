import sys
from collections import deque

def bfs():
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    while q:
        now = q.popleft()
        y, x = now[0], now[1]
        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x
            if dy < 0 or dx < 0  or dy >= Y or dx >= X: continue
            if MAP[dy][dx] == -1 or MAP[dy][dx] == 1: continue
            if MAP[dy][dx] == 0:
                MAP[dy][dx] = MAP[y][x] + 1
                q.append([dy, dx])
            else:
                if MAP[y][x] + 1 < MAP[dy][dx]:
                    MAP[dy][dx] = MAP[y][x] + 1
                    q.append([dy, dx])



X, Y  = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(Y)]

q = deque()
for i in range(Y):
    for j in range(X):
        if MAP[i][j] == 1:
            q.append([i,j])

bfs()


MAX = 0
flag = 0
for i in range(Y):
    for j in range(X):
        if MAP[i][j] == 0:
            flag = 1
        elif MAP[i][j] == MAX: continue
        else:
            if MAP[i][j] > MAX:
                MAX = MAP[i][j]

if flag:
    print(-1)
else:
    print(MAX-1)

