N = int(input()) # 큐브 사이즈
arr = [list(map(int, input().split())) for _ in range(N)] # 큐브에 적힌 숫자
dice = []
d = list(range(0, N)) # 큐브의 기본 좌표값 설정

for i in range(N):
    dice.append(d[i:] + d[:i]) # 큐브를 한칸씩 돌리는 배열 만들기


MAX = 0
tmp = [[0]*N for _ in range(N)] # 돌린 큐브의 값을 저장할 임시 변수

def dfs(level):
    global result, MAX, tmp
    if level == N: # 큐브 모든 줄을 탐색했을 때 리턴
        ret = 1
        for i in range(N):
            r = 0
            for j in range(N):
                r += tmp[j][i] # 한칸씩 값을 모두 더하여
            ret *= r # 더한 값을 곱해준다.
        if MAX < ret: # 최대값 찾는 코드
            MAX = ret
        return

    for i in range(N):
        for k in range(N):
            tmp[level][k] = arr[level][dice[i][k]] # 돌린 큐브의 값을 하나씩 저장해준다
        dfs(level+1)



dfs(0)
print(f'{MAX}점')