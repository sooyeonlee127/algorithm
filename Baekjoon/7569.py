import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs():
    global arr
    directz = [-1, 1, 0, 0, 0, 0]
    directy = [0, 0, -1, 1, 0, 0]
    directx = [0, 0, 0, 0, -1, 1]
    while q:
        now = q.popleft()
        z = now[0]
        y = now[1]
        x = now[2]

        for i in range(6):
            dz = directz[i] + z
            dy = directy[i] + y
            dx = directx[i] + x
            if dz < 0 or dy < 0 or dx < 0 or dz >= H or dy >= N or dx >= M: continue
            if arr[dz][dy][dx] == 0:
                arr[dz][dy][dx] = arr[z][y][x] + 1

                q.append([dz,dy,dx])




M, N, H = map(int, input().split())

arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for h in range(H)]
q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1:
                q.append([h,n,m])

bfs()
MAX = 0
flag = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 0:
                flag = 1
                break
            else:
                if arr[h][n][m] > MAX:
                    MAX = arr[h][n][m]
        if flag: break
    if flag: break

if flag:
    print(-1)
else:
    print(MAX-1)

