def dfs(level):
    global path, MIN
    if level == 3:
        if path[0] != '0':
            path = int(path)
            if path < MIN:
                MIN = path
        return

    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        backup = path
        path += str(num[i])
        dfs(level+1)
        used[i] = 0
        path = backup



N = int(input())
num = list(map(int, input().split()))
path = ''
MIN = 21e8
used = [0]*N
dfs(0)
print(MIN)