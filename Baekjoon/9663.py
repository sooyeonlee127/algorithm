def check(level):
    global bucket, N
    for i in range(level):
        if bucket[level] == bucket[i] or abs(bucket[level] - bucket[i]) == abs(level - i):
            return False
    return True


def dfs(level):
    global bucket, N, answer
    if level == N:
        answer += 1
        return
    for i in range(N):
        bucket[level] = i
        flag = check(level)
        if flag:
            dfs(level+1)



N = int(input())
bucket = [-100]*N
answer = 0
dfs(0)
print(answer)
