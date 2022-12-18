def equal_number(): # 같은 값을 찾는 함수
    global q
    directy = [-1, -1, -1, 0, 0, 1,1,1]
    directx = [-1,0,1,-1,1,-1,0,1]
    while q:
        now = q.pop(0)
        y, x = now[0], now[1]
        for i in range(8):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dy >= N or dx < 0 or dx >= M: continue
            if [dy, dx] in equal: continue
            if tmp != MAP[dy][dx]: continue
            q.append([dy, dx])
            used.append([dy,dx])
            equal.append([dy,dx])


def mountain(): # 같은 값 주변이 다 작은지 확인
    global mt, equal
    directy = [-1, -1, -1, 0, 0, 1,1,1]
    directx = [-1,0,1,-1,1,-1,0,1]
    while equal:
        now = equal.pop(0)
        y, x = now[0], now[1]
        for i in range(8):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dy >= N or dx < 0 or dx >= M: continue
            if MAP[dy][dx] > tmp:
                mt = False
                return


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
result = 0
used = []


for i in range(N):
    for j in range(M):
        if [i,j] in used: continue
        used.append([i,j])
        tmp = MAP[i][j]
        mt = True
        q = [[i,j]]
        equal = [[i,j]]
        equal_number()
        used += equal
        backup = equal[:]
        mountain()
        if mt:
            result += 1

print(result)


