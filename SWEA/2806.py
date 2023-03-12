import copy

# N-Queen의 규칙을 지켰는지 판별하는 함수
def check(x):
    global bucket
    # 현재 x좌표 전에 있는 값 중
    for i in range(x):
        # 겹치는 y좌표 값이 있는가 or 겹치는 대각선에 값이 놓여있는가 판별
        if bucket[i] == bucket[x] or abs(bucket[i] - bucket[x]) == abs(i-x):
            return False

    return True


# N-Queen의 위치를 입력하는 함수
def dfs(level): # level: 현재 queen이 놓인 수
    global answer, bucket
    if level == N: # queen이 N개만큼 놓였을 때
        answer += 1
        return
    
    for y in range(N):
        # bucket[x좌표] = y좌표
        bucket[level] = y
        flag = check(level)
        # 겹치는 값이 없다면, 다음 x좌표를 채워나간다.
        if flag:
            dfs(level+1)
        
            

T = int(input())
for tc in range(1, T+1):
    answer = 0
    N = int(input())
    # N-Queen의  위치를 받을 배열
    # 인덱스는 x좌표값, 인덱스에 입력되는 값은 y좌표값이다.
    bucket = [0]*N

    if N == 1:
        # N이 1일 경우 답은 1
        print(f'#{tc} 1')
    elif N == 0:
        # N이 0일 경우 답은 0
        print(f'#{tc} 0')
    else:
        # 그외의 경우 답을 구한다.
        dfs(0)
        print(f'#{tc} {answer}')
    