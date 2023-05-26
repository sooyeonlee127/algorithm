def dfs(level, total):
    global N, MIN, MAX
    if level == N-1:
        if total < MIN:
            MIN = total
        if total > MAX:
            MAX = total
        return
    

    for i in range(4):
        if MAP[i] > 0:
            if i == 0:
                tmp = total + NUM[level+1]
            elif i == 1:
                tmp = total - NUM[level+1]
            elif i == 2:
                tmp = total * NUM[level+1]
            else:
                if total < 0 and NUM[level+1] > 0:
                    tmp = (abs(total) // NUM[level+1]) * (-1)
                else:
                    tmp = total // NUM[level+1]
            MAP[i] -= 1
            dfs(level+1, tmp)
            MAP[i] += 1

N = int(input())
NUM = list(map(int, input().split()))
MAP = list(map(int, input().split()))
MAX = -21e8
MIN = 21e8
dfs(0,NUM[0])
print(MAX)
print(MIN)
