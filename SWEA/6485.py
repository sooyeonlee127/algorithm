T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop = [int(input()) for _ in range(P)]

    result = [0] * len(stop)
    for i in range(len(stop)):
        for k in range(len(bus)):
            if bus[k][0] <= stop[i] <= bus[k][1]:
                result[i] += 1
    print(f'#{tc} ', end='')
    print(*result)