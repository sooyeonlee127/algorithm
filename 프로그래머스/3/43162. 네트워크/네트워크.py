def solution(n, computers):
    answer = 0
    used = [0]*n
    for i in range(n):
        if used[i] == 1: continue
        dfs(i, computers, used)
        answer += 1
    return answer

def dfs(level, arr, used):
    used[level] = 1
    for i in range(len(arr)):
        if used[i] == 1: continue
        if arr[level][i] == 1:
            dfs(i, arr, used)
    
