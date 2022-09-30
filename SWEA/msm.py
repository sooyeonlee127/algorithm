import sys
sys.stdin = open('input.txt', 'r')

# [모의 SW 역량테스트] 미생물 격리


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0]*N for _ in range(N)]


    for k in range(K):
        a, b, c, d= map(int, input().split())
        arr[a][b] = [c,d]

    for m in range(M): # M 시간 반복
        tmp = [[[] for _ in range(N)] for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if arr[y][x] == 0: continue
                if arr[y][x][1] == 1:
                    if y == 1:
                        tmp[y-1][x].append([arr[y][x][0]//2, 2])
                    else:
                        tmp[y-1][x].append([arr[y][x][0], 1])
                elif arr[y][x][1] == 2:
                    if y == N-2:
                        tmp[y+1][x].append([arr[y][x][0]//2, 1])
                    else:
                        tmp[y+1][x].append([arr[y][x][0], 2])
                elif arr[y][x][1] == 3:
                    if x == 1:
                        tmp[y][x-1].append([arr[y][x][0]//2, 4])
                    else:
                        tmp[y][x-1].append([arr[y][x][0], 3])
                elif arr[y][x][1] == 4:
                    if x == N-2:
                        tmp[y][x+1].append([arr[y][x][0]//2, 3])
                    else:
                        tmp[y][x+1].append([arr[y][x][0], 4])


        for i in range(N):
            for j in range(N):
                if len(tmp[i][j]) != 0:
                    total = 0
                    max_idx = max(tmp[i][j])[1]
                    for k in range(len(tmp[i][j])):
                        total += tmp[i][j][k][0]
                    arr[i][j] = [total, max_idx]
                else:
                    arr[i][j] = 0
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue
            result += arr[i][j][0]

    print(f'#{tc} {result}')
