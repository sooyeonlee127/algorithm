import sys
sys.stdin = open('input.txt', 'r')

y, x = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(y)]
lst = []
for i in range(y):
    for j in range(x):
        lst.append([arr[i][j], (i, j)])



ret = sorted(lst, key=lambda x: (-x[0], x[1][0], x[1][1]))

for i in range(3):
    print(f'{ret[i][0]}({ret[i][1][0]},{ret[i][1][1]})')
