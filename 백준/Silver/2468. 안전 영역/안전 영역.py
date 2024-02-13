from collections import deque

N = int(input())
MAP = []
num_list = []
for _ in range(N):
    num = list(map(int, input().split()))
    num_list += num
    MAP.append(num)

num_list = list(set(num_list))
num_list = sorted(num_list)


answer = 1

for water in num_list[:len(num_list)-1]:
    result = 0
    used = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] <= water:
                used[i][j] = 1
    for i in range(N):
        for j in range(N):
            if used[i][j] == 0:
                result += 1
                q = deque()
                q.append([i,j])
                while q:
                    y,x = q.popleft()
                    used[y][x] = 1
                    for d in [[-1,0], [1,0], [0,-1], [0,1]]:
                        dy = y + d[0]
                        dx = x + d[1]
                        if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
                        if used[dy][dx] == 1: continue
                        q.append([dy,dx])
                        used[dy][dx] = 1
    answer = max(result, answer)
print(answer)
    