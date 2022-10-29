T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    box = list(map(int, input().split()))
    max = 0
    for idx in range(len(box)):
        cnt = 0
        for i in range(len(box) - 1, idx, -1):
            if box[i] >= box[idx]:
                cnt += 1
        if (N - 1) - idx - cnt > max:
            max = (N - 1) - idx - cnt

    print(f'#{test_case} {max}')