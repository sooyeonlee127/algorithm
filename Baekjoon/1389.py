N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
inf = N+1
MAP = [[inf]*(N+1) for _ in range(N+1)]

for i in range(M):
    MAP[arr[i][0]][arr[i][1]] = 1
    MAP[arr[i][1]][arr[i][0]] = 1

for k in range(N+1): # 경유
    for s in range(N+1): # 시작
        for d in range(N+1): # 도착
            if MAP[s][d] > MAP[s][k]+MAP[k][d]: # 경유를 한 경우가 더 가까울 때 경신
                MAP[s][d] = MAP[s][k]+MAP[k][d]

MIN = 21e8
result = [0]*(N+1)

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j: continue
        result[i] += MAP[i][j]

MIN = 21e8
MIN_idx = -1
for i in range(1, N+1):
    if MIN > result[i]:
        MIN = result[i]
        MIN_idx = i

print(MIN_idx)
