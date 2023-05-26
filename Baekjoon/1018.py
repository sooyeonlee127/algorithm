N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
BMAP = []
WMAP = []
Bstart = ['']*8
Wstart = ['']*8

for i in range(8):
    if i%2 == 0:
        Bstart[i] = 'B'
        Wstart[i] = 'W'
    else:
        Bstart[i] = 'W'
        Wstart[i] = 'B'


for i in range(8):
    if i%2 == 0:
        BMAP.append(Bstart)
        WMAP.append(Wstart)
    else:
        BMAP.append(Wstart)
        WMAP.append(Bstart)

MIN = 21e5
for sy in range(N-8+1):
    for sx in range(M-8+1):
        
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            for j in range(8):
                if BMAP[i][j] != MAP[i+sy][j+sx]:
                    cnt1+=1
                if WMAP[i][j] != MAP[i+sy][j+sx]:
                    cnt2+=1
        if MIN > cnt1:
            MIN = cnt1
        if MIN > cnt2:
            MIN = cnt2
        
print(MIN)
