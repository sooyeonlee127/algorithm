from collections import deque
import copy

def bfs(start, end):
    global used
    level = 0
    q = deque()
    q.append([start, level])
    while q:
        now = q.popleft()
        n, level = now[0], now[1]

        if n == end:
            return level

        backup = copy.deepcopy(n)
        n //= 2
        if 0 <= n <= 100000 and used[n] == 0:
            used[n] = 1
            q.append([n,level+1])
        n = backup

        n *= 2
        if 0 <= n <= 100000 and used[n] == 0:
            used[n] = 1
            q.append([n,level+1])
        n = backup

        n += 1
        if 0 <= n <= 100000 and used[n] == 0:
            used[n] = 1
            q.append([n,level+1])
        n = backup

        n -= 1
        if 0 <= n <= 100000 and used[n] == 0:
            used[n] = 1
            q.append([n,level+1])
        n = backup


S = int(input())
D = int(input())
used = [0]*100001
print(bfs(S,D))