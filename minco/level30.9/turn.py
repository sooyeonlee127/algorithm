
def tturn(arr):
    global cnt
    while arr != target:
        tmp = [[0]*3 for _ in range(3)]
        for y in range(3):
            for x in range(3):
                tmp[2-x][y] = arr[y][x]
        arr = tmp[:]
        cnt += 1




start = [list(map(int, input().split())) for _ in range(3)]
a = input()
target = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
tturn(start)
print(cnt)
