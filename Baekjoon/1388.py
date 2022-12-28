def bfs(sy, sx):
    directy1 = [-1,1] # 나무판자가 세로일 때 세로로 탐색
    directx1 = [0,0]
    directy2 = [0,0] # 나무판자가 가로일 때 가로로 탐색
    directx2 = [-1,1]
    q = [[sy,sx]]
    while q:
        now = q.pop(0)
        y,x = now[0], now[1]
        if MAP[y][x] == '|': # 세로일 때
            for i in range(2):
                dy = directy1[i] + y
                dx = directx1[i] + x
                if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
                if used[dy][dx] == 1: continue
                if MAP[dy][dx] == MAP[y][x]:
                    used[dy][dx] = 1
                    q.append([dy,dx])
        else: # 가로일 때
            for i in range(2):
                dy = directy2[i] + y
                dx = directx2[i] + x
                if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
                if used[dy][dx] == 1: continue
                if MAP[dy][dx] == MAP[y][x]:
                    used[dy][dx] = 1
                    q.append([dy,dx])




N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
used = [[0]*M for _ in range(N)] # 탐색한 지점 체크
result = 0 # 결과값 담을 변수
for i in range(N):
    for j in range(M):
        if used[i][j] == 1: continue # 탐색한 지점 다시보지 않음
        used[i][j] = 1
        bfs(i,j) # 연결된 나무판자를 모두 확인하면
        result += 1 # 하나의 나무판자임을 체크

print(result)
