import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T+1):
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    N = int(input())
    result = [0]*8
    level = 0
    cnt = 0
    print(f'#{tc}')
    while level < 8 :
        if N >= arr[level]:
            N -= arr[level]
            cnt += 1
        else:
            result[level] = cnt
            level+= 1
            cnt = 0
    print(*result)
