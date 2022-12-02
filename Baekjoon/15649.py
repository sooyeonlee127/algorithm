def check(level):
    global arr, used
    if level == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if used[i] == 1: continue
        used[i] = 1
        arr[level] = i
        check(level+1)
        used[i] = 0

N, M = map(int, input().split())

arr = [0]*M
used = [0]*(N+1)
check(0)
