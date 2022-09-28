import heapq


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[] for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s].append([e,w])

    st = 0
    ed = N
    result = [21e8]*(N+1)

    heap = []
    def dijkstra(start):
        heapq.heappush(heap, (0, start))
        result[start] = 0
        while heap:
            sk_cost, k = heapq.heappop(heap)
            if sk_cost > result[k]: continue
            if k >= N: continue
            for d in arr[k]:
                sd_cost = sk_cost + d[1]
                if sd_cost < result[d[0]]:
                    result[d[0]] = sd_cost
                    heapq.heappush(heap, (sd_cost, d[0]))
    dijkstra(st)
    print(f'#{tc} {result[ed]}')

