import sys
sys.stdin = open('input.txt', 'r')

def dfs(level, total):
    global MIN
    if level == N:
        if MIN > total:
            MIN = total
        return

    if total > MIN:
        return

    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        dfs(level+1, total+MAP[level][i])
        used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*N
    MIN = 21e8
    dfs(0,0)
    print(f'#{tc} {MIN}')