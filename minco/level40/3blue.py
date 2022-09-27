import sys
sys.stdin = open('input.txt', 'r')

def bfs(level):
    jump = [2,3,2]
    q = []
    q.append(level)
    while q:
        now = q.pop(0)
        if now == 0:
            for i in range(2):
                go = now + jump[i]
                if max(MAP[go] + lst[now], lst[go]) == MAP[go] + lst[now]:
                    lst[go] = max(MAP[go] + lst[now], lst[go])
                    q.append(go)
        else:
            for i in range(3):
                if i == 2:
                    go = now * jump[i]
                else:
                    go = now + jump[i]
                if go < 12 :
                    if max(MAP[go] + lst[now], lst[go]) == MAP[go] + lst[now]:
                        lst[go] = max(MAP[go] + lst[now], lst[go])
                        q.append(go)




MAP = list(map(int, input().split()))
lst = [-21e8]*12
lst[0] = 0
MAX = 0
bfs(0)
print(max(lst))




