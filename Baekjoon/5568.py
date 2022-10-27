import sys, copy
sys.stdin = open('input.txt', 'r')

def dfs(level, total):
    global result
    if level == K:
        if total not in result:
            result.append(total)
        return

    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        dfs(level+1, total+arr[i])
        used[i] = 0


N = int(input())
K = int(input())
arr = [input() for _ in range(N)]
used = [0]*N
result = []
dfs(0,'')
print(len(result))