import copy

arr = [list(input()) for _ in range(4)]
N = int(input())
path = ['']*N
visit = [[0]*4 for _ in range(4)]
MAX = 0
cnt = 0
result = []

def dfs(level, total):
    global MAX, visit, arr, path, result, cnt
    directy = [1, -1, 0, 0, 0]
    directx = [0, 0, 0, -1, 1]
    if level == N:
        if total > MAX:
            MAX = total
            result = copy.deepcopy(path)
        return
    backup = copy.deepcopy(arr)
    for i in range(4):
        for j in range(4):
            if visit[i][j] == 0 and arr[i][j] != '_':
                path[level] = copy.deepcopy(arr[i][j])
                visit[i][j] = 1
                cnt = 0
                for k in range(5):
                    dy = directy[k] + i
                    dx = directx[k] + j
                    if 0 <= dy < 4 and 0 <= dx < 4 and arr[dy][dx] != '_':
                        cnt += 1
                        arr[dy][dx] = '_'
                dfs(level+1, total+cnt)
                path[level] = ''
                visit[i][j] = 0
                arr = copy.deepcopy(backup)



dfs(0, 0)
result.sort()
for i in range(len(result)):
    print(result[i], end=' ')
print()