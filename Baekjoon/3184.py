def bfs(sy,sx):
    global cnt1, cnt2
    q.append([sy,sx])
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    while q:
        now = q.pop(0)
        y = now[0]
        x = now[1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dy >= R or dx < 0 or dx >= C: continue
            if MAP[dy][dx] == '#': continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            if MAP[dy][dx] == 'o':
                cnt1 += 1
            elif MAP[dy][dx] == 'v':
                cnt2 += 1
            q.append([dy,dx])



R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
used = [[0]*C for _ in range(R)]
q = []

result1 = 0
result2 = 0

for i in range(R):
    for j in range(C):
        if used[i][j] == 0 and MAP[i][j] != '#':
            used[i][j] = 1
            if MAP[i][j] == '.':
                cnt1, cnt2 = 0,0
                bfs(i,j)
            elif MAP[i][j] == 'o':
                cnt1, cnt2 = 1,0
                bfs(i,j)
            else:
                cnt1, cnt2 = 0, 1
                bfs(i,j)
            if cnt1 > cnt2:
                result1 += cnt1
            else:
                result2 += cnt2


print(result1, result2)
