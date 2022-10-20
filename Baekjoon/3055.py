from collections import deque
import copy
import sys


def bfs():
    global q, MAP, MAP2
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    while q:
        tmp = q.popleft()
        y, x, now, level = tmp[0], tmp[1], tmp[2], tmp[3]
        # y = y좌표, x = x좌표, now = S or *, level = 거리

        if now == 'S': # 고슴도치가 가는 길일 경우
            for k in range(4):
                dy = directy[k] + y
                dx = directx[k] + x
                if dx < 0 or dy < 0 or dx >= C or dy >= R: continue # 배열 벗어나는지 확인
                if MAP2[dy][dx] == '*': continue # 물길 있으면 x
                if MAP[dy][dx] == 'D': return level + 1 # 도착지이면 거리를 출력한다
                if MAP[dy][dx] == '.': # 길이면
                    MAP[dy][dx] = 'S' # 고슴도치가 있음을 표시
                    q.append([dy, dx, 'S', level+1])


        elif now == '*':
            for k in range(4):
                dy = directy[k] + y
                dx = directx[k] + x
                if dx < 0 or dy < 0 or dx >= C or dy >= R: continue# 배열 벗어나는지 확인
                if MAP2[dy][dx] == '.': # 길이면
                    MAP2[dy][dx] = '*'  # 물길임을 표시
                    q.append([dy, dx, '*', 0])



R, C = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline()) for _ in range(R)]
MAP2 = copy.deepcopy(MAP) # 같은 배열을 두 개 만들어 준다
# MAP: 고슴도치가 지나가는 길 표시, MAP2: 물이 퍼지는 길 표시


q = deque()
start = deque()
water = deque()

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'S':
            start.append([i,j,'S', 0])
        elif MAP[i][j] == '*':
            water.append([i,j,'*', 0])


q += water # q에 물이 있는 곳 먼저 추가
for i in range(len(start)):
    q.append(start[i]) # 고슴도치가 있는 곳 추가
# 물이 번지기 직전인 곳도 고슴도치가 갈 수 없기 때문에 물길을 먼저 추가함



ret = bfs()

if ret == None: # 리턴값이 없을 때 즉, 최단경로를 찾지 못했을 때
    print('KAKTUS')
else: # 리턴 값이 있을 때
    print(ret)

