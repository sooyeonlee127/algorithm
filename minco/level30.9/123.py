def dfs(level):
    global cnt
    if level == 3:
        cnt += 1
        return

    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        dfs(level+1)
        used[i] = 0

N = int(input())
cnt = 0
used = [0]*N
dfs(0)
print(cnt)
