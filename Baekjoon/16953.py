def dfs(level, start):
    global MIN
    if start > B: return
    if level > MIN: return
    if start == B:
        if level < MIN:
            MIN = level
        return


    for i in range(2):
        if i == 0:
            dfs(level+1, start*2)
        else:
            dfs(level+1, start*10+1)


A, B = map(int, input().split())
MIN = 21e8
dfs(0,A)

if MIN == 21e8:
    print(-1)
else:
    print(MIN+1)
