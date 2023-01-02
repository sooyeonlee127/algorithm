def dfs(s,t, cnt):
    global MIN
    if s == t:
        if MIN > cnt:
            MIN = cnt
        return
    if s > t:
        return

    for i in range(2):
        if i == 0:
            dfs(s*2, t+3, cnt+1)
        else:
            dfs(s+1, t, cnt+1)



T = int(input())
for tc in range(T):
    S, T = map(int, input().split())
    MIN = 21e8
    dfs(S,T,0)
    print(MIN)
