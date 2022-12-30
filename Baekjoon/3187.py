def bfs(sy,sx):
    global k_cnt, v_cnt
    q = [[sy,sx]]
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    while q:
        now = q.pop(0)
        y,x = now[0], now[1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dx < 0 or dy >= R or dx >= C: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            if MAP[dy][dx] == '#': continue
            if MAP[dy][dx] == 'k':
                k_cnt += 1
                MAP[dy][dx] = 'kk'
            elif MAP[dy][dx] == 'v':
                v_cnt += 1
                MAP[dy][dx] = 'vv'
            q.append([dy, dx])


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
v_list = []
used = [[0]*C for _ in range(R)]
v_cnt = 0
k_cnt = 0
v_result = 0
k_result = 0

for i in range(R):
    for j in range(C):
        if MAP[i][j] == '#': continue
        if used[i][j] == 1: continue
        v_cnt = 0
        k_cnt = 0
        bfs(i,j)
        if v_cnt < k_cnt:
            k_result += k_cnt
        else:
            v_result += v_cnt

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'v':
            v_result += 1
        elif MAP[i][j] == 'k':
            k_result += 1




print(k_result, v_result)
