def dfs(level, total, p):
    global MIN, used
    ret = 0
    if level == N-1:
        for i in range(len(p)-1):
            ret += arr[path[i]][path[i+1]]
        if ret < MIN:
            MIN = ret
        return

    for i in range(1, N):
        if used[i] == 1: continue
        used[i] = 1
        p[level+1] = i
        dfs(level+1, total+arr[level][i], p)
        used[i] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    used = [0]*N
    arr = [list(map(int, input().split())) for _ in range(N)]
    MIN = 21e8
    path = [0]*(N+1)
    dfs(0, 0, path)
    print(f'#{tc} {MIN}')