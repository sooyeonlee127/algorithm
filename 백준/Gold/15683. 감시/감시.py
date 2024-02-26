from copy import deepcopy

Y, X = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(Y)]
result_map = [[0]*X for _ in range(Y)]

order = { 1: [[1],[2],[3],[4]], 2: [[1,3],[2,4]], 3: [[1,2],[2,3],[3,4],[4,1]], 4:[[2,3,4],[1,3,4],[1,2,4],[1,2,3]], 5:[[1,2,3,4]] }
direct = {1: [-1,0], 2: [0,-1], 3:[1,0], 4:[0,1] } 

cnt = 0
cctv = []
MIN = 21e5
for i in range(Y):
    for j in range(X):
        if MAP[i][j] == 0: continue
        result_map[i][j] = 1
        if MAP[i][j] == 6: continue
        cctv.append([MAP[i][j], i, j])


def dfs(level, arr):
    global cctv, MAP, Y, MIN, X
    if level == len(cctv):
        tmp = 0
        for i in range(Y):
            tmp += arr[i].count(0)
        MIN = min(MIN, tmp)
        return
    now = cctv[level][0]
    y,x = cctv[level][1], cctv[level][2]
    for lst in order[now]:
        backup = deepcopy(arr)
        for i in lst:
            dy = y + direct[i][0]
            dx = x + direct[i][1]
            while dy >= 0 and dx >= 0 and dy < Y and dx < X:
                if MAP[dy][dx] == 6: break
                backup[dy][dx] = 1
                dy += direct[i][0]
                dx += direct[i][1]
        dfs(level+1, backup)


dfs(0, result_map)
print(MIN)