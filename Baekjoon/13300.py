N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result_b = []
result_g = []
result = []
for i in range(N):
    if arr[i][0] == 1:
        result_b.append(arr[i][1])
    else:
        result_g.append(arr[i][1])

for i in range(1, 7):
    if result_g.count(i) / K > result_g.count(i) // K:
        result.append((result_g.count(i)//K) +1)
    else:
        result.append((result_g.count(i)//K))
    if result_b.count(i) / K > result_b.count(i) // K:
        result.append(result_b.count(i) // K +1)
    else:
        result.append((result_b.count(i) // K))


print(sum(result))