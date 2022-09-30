from collections import deque

def bfs(fnum, fcnt):
    global MIN
    used = [0]*1000001
    q=deque()
    q.append([fnum, fcnt])
    while q:
        now = q.popleft()
        num = now[0]
        cnt = now[1]
        if num == target:
            if MIN > cnt:
                MIN = cnt
            return
        if cnt > MIN:
            return

        lst = [num+1, num-1, num*2, num-10]
        for i in range(4):
            if 1000000 < lst[i] or lst[i] < 0 : continue
            if used[lst[i]] == 1: continue
            used[lst[i]] = 1
            q.append([lst[i], cnt+1])

T = int(input())
for tc in range(1, T+1):
    first, target = map(int, input().split())
    MIN = 21e8
    memo = []
    bfs(first, 0)
    print(f'#{tc} {MIN}')