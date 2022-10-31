import sys
sys.stdin = open('input.txt', 'r')

def dfs(level, start, total1, total2):
    global MIN
    if level > 0 and abs(total1 - total2) < MIN:
        MIN = abs(total1 - total2)


    for i in range(start, N):
        dfs(level+1, i+1, total1*lst1[i], total2+lst2[i])



N = int(input())
lst1 = [0]*N
lst2 = [0]*N
MIN = 21e8
for i in range(N):
    lst1[i], lst2[i] = map(int, input().split())

dfs(0, 0,1,0)
print(MIN)

