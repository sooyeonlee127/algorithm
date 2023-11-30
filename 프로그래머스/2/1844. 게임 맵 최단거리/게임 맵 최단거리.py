from collections import deque
def solution(maps):
    answer = bfs(0,0,0,maps)
    return answer

def bfs(sy,sx, cnt, MAP):
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    used = [[0]*len(MAP[0]) for _ in range(len(MAP))]
    q = deque()
    q.append([sy,sx, 1])
    used[sy][sx] = 1
    while q:
        y,x,now = q.popleft()
        if y == len(MAP)-1 and x == len(MAP[0])-1:
            return now
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy >= len(MAP) or dy < 0 or dx >= len(MAP[0]) or dx < 0: continue
            if MAP[dy][dx] == 0: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy, dx, now+1])

    return -1
        
        
