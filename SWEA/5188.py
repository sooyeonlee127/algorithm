def dfs(y, x, total):
    global MIN, used
    directy = [0, 1]
    directx = [1, 0]
    if y == N-1 and x == N-1:
        if total < MIN:
            MIN = total
        return

    for i in range(2):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy < 0 or dx <0 or dx >= N or dy >= N: continue
        if used[dy][dx] == 1: continue
        used[dy][dx] = 1
        dfs(dy, dx, total+arr[dy][dx])
        used[dy][dx] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    used = [[0]*N for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    MIN = 21e8
    used[0][0] = 1
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {MIN}')