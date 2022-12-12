import sys
sys.stdin = open('input.txt', 'r')

def bfs():
    directy = [-1,-1,-1,0,0,1,1,1]
    directx = [-1,0,1,-1,1,-1,0,1]
    while q:
        now = q.pop(0)
        y = now[0]
        x = now[1]
        for i in range(8):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
            if MAP[dy][dx] != 0: continue
            MAP[dy][dx] = MAP[y][x] + 1
            q.append([dy,dx])


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
q = []

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            q.append([i,j])
bfs()
MAX = 0
for i in range(N):
    for j in range(M):
        if MAX < MAP[i][j]:
            MAX = MAP[i][j]

print(MAX-1)
