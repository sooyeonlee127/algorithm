N = int(input())
time = []
for i in range(N):
    time.append(list(map(int, input().split())))

timetable = sorted(time, key=lambda x: x[1])

cnt = 0
beforetime = -1
for i in range(N):
    if beforetime <= timetable[i][0]:
        beforetime = timetable[i][1]
        cnt += 1

print(cnt)