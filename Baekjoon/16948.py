def bfs(sy,sx):
    global result
    directy = [-2, -2, 0, 0, 2, 2] # 이동할 수 있는 위치
    directx = [-1, 1, -2, 2, -1, 1]
    q = [[sy,sx]]
    while q:
        now = q.pop(0)
        y,x = now[0], now[1]
        for i in range(6):
            dy=y+directy[i]
            dx=x+directx[i]
            if dy < 0 or dx < 0 or dy >= N or dx >= N:continue
            if dy == r2 and dx == c2: # 목적지에 도착하면
                result = MAP[y][x] + 1 # 현재 위치까지 걸음수 변수에 할당
                return
            if MAP[dy][dx] != 0: continue
            MAP[dy][dx] = MAP[y][x] + 1
            q.append([dy,dx])

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
MAP = [[0]*N for _ in range(N)]
result = -1
bfs(r1,c1)
print(result)
