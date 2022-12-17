def bfs(sy,sx):
    q.append([sy,sx])
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    while q:
        now = q.pop(0)
        y,x = now[0], now[1]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dy >= N or dx < 0 or dx >= N: continue
            if used[dy][dx] == 1: continue
            if MAP[dy][dx] not in target: continue
            used[dy][dx] = 1
            q.append([dy,dx])

def bfs2(sy,sx):
    q.append([sy,sx])
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    while q:
        now = q.pop(0)
        y,x = now[0], now[1]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dy >= N or dx < 0 or dx >= N: continue
            if used2[dy][dx] == 1: continue
            if MAP[dy][dx] not in target: continue
            used2[dy][dx] = 1
            q.append([dy,dx])





N = int(input())
MAP = [list(input()) for _ in range(N)]
used = [[0]*N for _ in range(N)]
used2 = [[0]*N for _ in range(N)]
target = []
q = []
result1 = 0
result2 = 0
for i in range(N):
    for j in range(N):
        if used[i][j] == 1: continue
        tmp = MAP[i][j]
        if tmp == 'B':
            target = ['B']
            used[i][j] = 1
            bfs(i,j)
            result1 +=1
            result2 +=1
        else:
            target = ['G', 'R']
            bfs(i,j)
            result2 += 1

for i in range(N):
    for j in range(N):
        if used2[i][j] == 1: continue
        if MAP[i][j] == 'G':
            target = ['G']
            used2[i][j] = 1
            bfs2(i,j)
            result1 += 1
        elif MAP[i][j] == 'R':
            target = ['R']
            used2[i][j] = 1
            bfs2(i,j)
            result1 += 1



print(result1, result2)
