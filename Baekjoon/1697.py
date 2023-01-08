from collections import deque



def bfs():
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if target == now:
            print(bucket[now])
            return
        for jump in (now - 1, now + 1, now * 2):
            if 0 <= jump <= MAX and not bucket[jump]:
                bucket[jump] = bucket[now] + 1
                q.append(jump)


start, target = map(int, input().split())
MAX = 10 ** 5
bucket = [0] * (MAX+1)
bfs()
