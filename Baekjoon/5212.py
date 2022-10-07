def check(y, x):
    cnt = 0
    direct_y = [0, 0, 1, -1]
    direct_x = [1, -1, 0, 0]
    for i in range(4):
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if 0 <= dx < C+2 and 0 <= dy < R+2:
            if new_arr[dy][dx] == '.':
                cnt += 1
        if cnt >= 3:
            new_arr[y][x] = '*'


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
new_arr = [['.']*(C+2) for _ in range(R+2)]

for i in range(R):
    for j in range(C):
        new_arr[i+1][j+1] = arr[i][j]



for i in range(len(new_arr)):
    for j in range(len(new_arr[0])):
        if new_arr[i][j] == 'X':
            check(i,j)



y = []
x = []

for i in range(R+2):
    for j in range(C+2):
        if new_arr[i][j] == 'X':
            y.append(i)
            x.append(j)



for i in range(min(y), max(y)+1):
    for j in range(min(x), max(x)+1):
        if new_arr[i][j] == '*':
            new_arr[i][j] = '.'
        print(new_arr[i][j], end='')
    print()