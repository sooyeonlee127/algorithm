def bfs(sy,sx):
    global cnt
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    q = [[sy,sx]]
    while q:
        now = q.pop(0)
        y,x = now[0], now[1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
            if MAP[dy][dx] == 1:
                MAP[dy][dx] += 1
                cnt += 1
                q.append([dy,dx])




N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
MAX = 0 # 가장 넓은 그림의 넓이를 담는 변수
painting = 0 # 그림의 수를 세는 변수
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            cnt = 1
            MAP[i][j] += 1
            painting += 1 # if문에 들어오면 그림이 하나 더 있는 것이므로 세어준다
            bfs(i,j)
            if cnt > MAX: # 함수를 통해 센 cnt가 MAX보다 크면
                MAX = cnt # 경신해준다.

print(painting)
print(MAX)
