import sys
sys.stdin = open("input.txt", "r")


def babygin(arr, player):
    for i in range(2, 10):
        if arr[i - 2] != 0 and arr[i - 1] != 0 and arr[i] != 0:
            return player
    for k in range(10):
        if arr[k] == 3:
            return player
    return 0


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    counts_1 = [0]*10
    counts_2 = [0]*10
    ret = 0
    for i in range(len(card)):
        if i % 2 == 0:
            counts_1[card[i]] += 1
            ret += babygin(counts_1, 1)
        else:
            counts_2[card[i]] += 1
            ret += babygin(counts_2, 2)

        if ret == 3:
            print(f'#{tc} {0}')
            break
        elif ret == 1:
            print(f'#{tc} {1}')
            break
        elif ret == 2:
            print(f'#{tc} {2}')
            break
    if ret == 0:
        print(f'#{tc} {0}')