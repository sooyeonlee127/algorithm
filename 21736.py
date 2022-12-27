def bfs(starty, startx):
    global cnt
    q = [[starty, startx]]
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    while q:
        now = q.pop(0)
        y,x = now[0],now[1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            if MAP[dy][dx] == 'P': # 사람이 있으면
                cnt += 1 # 수를 세고
                q.append([dy,dx]) # 이동한다
            elif MAP[dy][dx] == 'O': # 길이면
                q.append([dy,dx]) # 이동한다




N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
used = [[0]*M for _ in range(N)]
cnt = 0
sy, sx = 0,0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'I': # 도연이가 있는 곳을
            sy, sx = i, j # 시작점으로 한다.
            used[sy][sx] = 1
            break

bfs(sy,sx)

if cnt: # 만난 친구가 있으면
    print(cnt)
else: # 없으면
    print('TT')
