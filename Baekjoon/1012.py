import sys
sys.stdin = open('input.txt', 'r')

def bfs(sy, sx):
    global num
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    q = []
    q.append([sy, sx])
    while q:
        now = q.pop(0)
        y,x = now[0], now[1]
        MAP[y][x] = num
        used[y][x] = 1
        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            if MAP[dy][dx] != 0:
                MAP[dy][dx] = num
                q.append([dy,dx])






T = int(input())
for tc in range(1,T+1):
    M, N, K = map(int, input().split())
    MAP = [[0]*M for _ in range(N)]
    used = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        MAP[b][a] = 1

    num = 5
    lst = []
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                used[i][j] = 1
                lst.append(num)
                bfs(i, j)
                num += 1



    print(len(lst))