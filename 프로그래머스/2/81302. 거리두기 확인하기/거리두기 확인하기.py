from collections import deque

used = [[0]*5 for _ in range(5)]
directy = [-1,1,0,0]
directx = [0,0,-1,1]
MAP = []
def bfs(y,x, st):
    global MAP, used
    q = deque()
    q.append([y, x, st])
    used[y][x] = 1
    while q:
        sy, sx, step = q.popleft()
        for i in range(4):
            dy = directy[i] + sy
            dx = directx[i] + sx
            if dy < 0 or dx < 0 or dy >= 5 or dx >= 5: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            if MAP[dy][dx] == 'X': continue
            if MAP[dy][dx] == 'P' and step < 2:
                # print('false', dy,dx,step)
                return False
            if step < 2:
                q.append([dy,dx, step + 1])
    return True
    


def solution(places):
    global MAP, used
    answer = []
    for t in range(5):
        result = True
        MAP = places[t]
        for i in range(5):
            if result == False: break
            for j in range(5):
                used = [[0]*5 for _ in range(5)]
                if result == False: break
                if places[t][i][j] == 'P':
                    result = bfs(i,j,0)
                    
        if result:
            answer.append(1)
        else:
            answer.append(0)
                
    
    
    return answer