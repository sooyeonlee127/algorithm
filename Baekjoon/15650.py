def dfs(level, start):
    if level == M:
        print(*tmp)
        return

    for i in range(start, N+1):
        tmp[level] = i
        dfs(level+1, i+1)


N, M = map(int, input().split())
used = [0]*(N+1)
tmp = [0]*M
dfs(0,1)


