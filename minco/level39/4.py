N = int(input())
arr = list(map(int, input().split()))
result = 100

arr.sort()
cnt = 0
for i in range(N):
    tmp = result - arr[i]
    if tmp >= 0:
        result = tmp
        cnt += 1
print(cnt)