
Y, X = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(Y)]
MAX = 0

def check(y,x):
    global MAX, MAP, Y, X
    # 4개
    if y+4 <= Y:
        tmp = 0
        for i in range(y,y+4):
            tmp += MAP[i][x]
        MAX = max(MAX, tmp)
    if x+4 <= X:
        tmp = sum(MAP[y][x:x+4])
        MAX = max(MAX, tmp)
    # 3개
    if y+2 <= Y and x+3 <= X:
        # 000
        # 000
        tmp = 0
        for i in range(y,y+2):
            tmp += sum(MAP[i][x:x+3])
        MAX = max(MAX, tmp - MAP[y][x] - MAP[y+1][x+2])
        MAX = max(MAX, tmp - MAP[y][x+2] - MAP[y+1][x])
        MAX = max(MAX, tmp - MAP[y][x] - MAP[y][x+2])
        MAX = max(MAX, tmp -  MAP[y+1][x] - MAP[y+1][x+2])

        MAX = max(MAX, tmp - sum(MAP[y][x:x+2]))
        MAX = max(MAX, tmp - sum(MAP[y][x+1:x+3]))
        MAX = max(MAX, tmp - sum(MAP[y+1][x:x+2]))
        MAX = max(MAX, tmp - sum(MAP[y+1][x+1:x+3]))
        MAX = max(MAX, tmp - MAP[y][x] - MAP[y+1][x])
        MAX = max(MAX, tmp - MAP[y][x+2] - MAP[y+1][x+2])
    if y+3 <= Y and x+2 <= X:
        # 00
        # 00
        # 00
        tmp = 0
        for i in range(y,y+3):
            tmp += sum(MAP[i][x:x+2])
        MAX = max(MAX, tmp - MAP[y][x] - MAP[y+2][x+1])
        MAX = max(MAX, tmp - MAP[y][x+1] - MAP[y+2][x])
        
        MAX = max(MAX, tmp - MAP[y][x] - MAP[y+2][x])
        MAX = max(MAX, tmp - MAP[y][x+1] - MAP[y+2][x+1])


        MAX = max(MAX, tmp - MAP[y][x] - MAP[y+1][x])
        MAX = max(MAX, tmp - MAP[y][x+1] - MAP[y+1][x+1])
        MAX = max(MAX, tmp - MAP[y+1][x] - MAP[y+2][x])
        MAX = max(MAX, tmp - MAP[y+1][x+1] - MAP[y+2][x+1])
for i in range(Y):
    for j in range(X):
        check(i,j)
print(MAX)