import sys
sys.stdin = open('input.txt', 'r')

def dfs(level):
    global path
    if level == 3:
        print(*path)
        return

    for i in range(3):
        path[level] = name[i]
        dfs(level+1)



name = list(input().split())
path = ['']*3
dfs(0)