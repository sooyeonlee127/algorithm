N = int(input())
arr = [[0]*N for _ in range(N)]
y1, x1, y2, x2 = map(int, input().split())

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
q = []

q.append([y1,x1, 1])
q.append([y2,x2, 1])

while q:
    now = q.pop(0)
    y, x, level = now[0], now[1], now[2]
    arr[y][x] = level
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if 0 > dy or dy >= N or 0 > dx or dx >= N: continue
        if arr[dy][dx] == 0:
            q.append([dy, dx, level+1])

for i in range(N):
    for j in range(N):
        print(arr[i][j], end='')
    print()
