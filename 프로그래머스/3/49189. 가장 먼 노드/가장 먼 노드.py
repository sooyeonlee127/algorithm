from collections import deque
def solution(n, edge):
    lst = [[] for _ in range(n+1)]
    result = [0]*(n+1)
    for e in edge:
        lst[e[0]].append(e[1])
        lst[e[1]].append(e[0])
    result[1] = 1
    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        for n in lst[now]:
            if result[n] == 0:
                queue.append(n)
                result[n] = result[now] + 1
    return result.count(max(result))

