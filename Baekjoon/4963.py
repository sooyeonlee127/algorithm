def bfs(sy,sx):
    global cnt
    directy = [-1, -1, -1, 0, 0, 1, 1, 1]
    directx = [-1, 0, 1, -1, 1, -1, 0, 1]
    q = [[sy,sx]]
    cnt += 1
    while q:
        now = q.pop(0)
        y, x = now[0], now[1]
        for i in range(8):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dx < 0 or dy >= h or dx >= w: continue
            if MAP[dy][dx] != 1: continue
            MAP[dy][dx] += 1 # 이미 확인한 부분은 다음에 확인하지 않도록 수를 바꾸어준다.
            q.append([dy,dx])



while 1:
    try: # 테스트 케이스가 몇 개인지 모르기 때문에 try, except를 사용한다.
        w, h = map(int, input().split())
        if w == 0 or h == 0: break # 탐색을 아예 안하는 경우는 출력을 하지 않는다.
        MAP = [list(map(int, input().split())) for _ in range(h)]
        cnt = 0
        for i in range(h):
            for j in range(w):
                if MAP[i][j] == 1:
                    bfs(i,j)
        print(cnt)

    except:
        break
