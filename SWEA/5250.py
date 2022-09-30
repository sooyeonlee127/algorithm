import sys
sys.stdin = open('input.txt', 'r')

def dfs(sy,sx):
    global MAP, result
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    q = []
    q.append([sy,sx])
    while q:
        now = q.pop(0)
        y,x = now[0], now[1]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dx < 0 or dx >= N or dy >= N: continue
            if MAP[dy][dx] - MAP[y][x] > 0:
                if result[dy][dx] > (result[y][x] + MAP[dy][dx] - MAP[y][x] + 1):
                    result[dy][dx] = (result[y][x] + MAP[dy][dx] - MAP[y][x] + 1)
                    q.append([dy,dx])
            else:
                if result[dy][dx] > (result[y][x] + 1):
                    result[dy][dx] = (result[y][x] + 1)
                    q.append([dy,dx])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    result = [[21e8]*N for _ in range(N)]
    result[0][0] = 0
    dfs(0,0)
    print(f'#{tc} {result[N-1][N-1]}')
