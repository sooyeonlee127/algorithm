import sys
sys.stdin = open('input.txt', 'r')


def bfs(sy, sx):
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = []
    q.append([sy, sx])
    while q:
        now = q.pop(0)
        y, x = now[0], now[1]
        MAP[y][x] = num
        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            if MAP[dy][dx] == 1:
                MAP[dy][dx] = num
                q.append([dy, dx])


N = int(input())
MAP = [list(map(int, input())) for _ in range(N)]
used = [[0]*N for _ in range(N)]
num = 5
lst = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and used[i][j] == 0:
            used[i][j] = 1
            lst.append(num)
            bfs(i, j)
            num += 1
ret = len(lst)
print(ret)

result = []
for k in range(ret):
    total = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == lst[k]:
                total += 1
    result.append(total)

result.sort()
for i in range(ret):
    print(result[i])