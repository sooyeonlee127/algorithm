import sys
sys.stdin = open("input.txt", "r")



def dfs(level, now, cnt):
    global MIN
    if cnt >= MIN:
        return

    if level == N-1:
        if MIN > cnt:
            MIN = cnt
        return

    for i in range(now, 0, -1):
        dx = level+ i
        if dx > N-1: continue
        if dx == N-1: dfs(dx, 0, cnt)
        else:
            dfs(dx, lst[dx], cnt+1)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    lst = arr[1:]
    lst.append(0)
    used = [0]*N
    used[0] = 1
    MIN = 21e8
    charge = [0] * N
    charge[0] = lst[0]
    dfs(0,lst[0], 0)
    print(f'#{tc} {MIN}')




