import sys
sys.stdin = open('input.txt', 'r')


def dfs(level, start):
    global word, cnt
    if level == 4:
        if word == 'CHRISTMAS':
            cnt += 1
        return

    for i in range(start, N):
        backup = word
        word += arr[i]
        dfs(level+1, i+1)
        word = backup


N = int(input())
arr = [input() for _ in range(N)]
word = ''
cnt = 0
dfs(0,0)
print(cnt)