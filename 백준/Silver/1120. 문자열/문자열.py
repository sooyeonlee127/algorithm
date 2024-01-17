X, Y = map(str, input().split())
cnt = len(Y) - len(X)
MIN = 21e5
for i in range(0, cnt+1):
    tmp = 0    
    for j in range(len(X)):
        if X[j] != Y[j+i]:
            tmp += 1
    if tmp < MIN:
        MIN = tmp
        bestStart = i
        bestEnd = i+len(X)

print(MIN)