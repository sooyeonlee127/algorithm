def dfs(level):
    global cnt
    for i in range(N+1):
        if used[i] == 1: continue
        if MAP[level][i] == 1:
            used[i] = 1
            dfs(i)


N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
MAP = [[0]*(N+1) for _ in range(N+1)]
used = [0]*(N+1)

for i in range(M):
    MAP[arr[i][0]][arr[i][1]] = 1 # dfs로 탐색하기 위해 체크해 준다.
    MAP[arr[i][1]][arr[i][0]] = 1 # 양방향 탐색하기 위해 반대로도 체크해준다.

used[1] = 1
dfs(1)

result = 0
for i in range(N+1):
    if used[i] == 1: # 바이러스가 있다고 체크된 곳의 수를 세어준다.
        result += 1

print(result - 1) # 바이러스가 있는 컴퓨터의 수 - 1번 컴퓨터
