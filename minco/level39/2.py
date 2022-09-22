coin = [1,5,10,50]
num = int(input())
idx = (num // 10) + 1
bucket = [[0]*idx for _ in range(5)]

for i in range(idx):
    bucket[0][i] += i

for k in range(1, 5):
    for i in range(1, idx):
        mok = i // coin[k-1]
        if i % coin[k-1] == 0:
            bucket[k][i] = i // coin[k-1]
        else:
            if mok == 0:
                bucket[k][i] = bucket[k-1][i]
            else:
                bucket[k][i] = min(bucket[k-1][i], bucket[k][i % coin[k-1]] + mok)


print(bucket[4][idx-1])