import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    time = sorted(arr, key=lambda x: x[1])
    cnt = 1
    s  = time[0][1]
    for i in range(1, N):
        if s <= time[i][0]:
            cnt += 1
            s = time[i][1]
    print(f'#{tc} {cnt}')