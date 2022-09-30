import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
result = [[0]*N for _ in range(N)]

for k in range(N):
    for s in range(N):
        for d in range(N):
            if arr[s][k] == 1 and arr[k][d] == 1:
                arr[s][d] = 1

for i in range(N):
    print(*arr[i])