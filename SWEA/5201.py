import sys
sys.stdin = open("input.txt", "r")

def check(m, s):
    for i in range(s, N):
        if w[i] <= m:
            s = i + 1
            return [w[i], s]
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 트럭수 M, 화물 수 N
    w = list(map(int, input().split())) # 화물 무게
    t = list(map(int, input().split())) # 적재용량
    w.sort(reverse=True)
    t.sort(reverse=True)
    cnt = 0
    now = []
    start = 0
    for i in range(M):
        now = check(t[i], start)
        if now != 0 :
            cnt += now[0]
            start = now[1]
    print(f'#{tc} {cnt}')

