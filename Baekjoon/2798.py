N, M = map(int, input().split())
num = list(map(int, input().split()))
total = 0
result = []

for i in range(len(num)):
    for j in range(i+1, len(num)):
        total = 0
        for k in range(j+1, len(num)):
            total = num[i] + num[j] + num[k]
            if total <= M:
                result.append(total)

MAX = 0
for i in range(len(result)):
    if MAX <= result[i]:
        MAX = result[i]

print(MAX)
