import sys
sys.stdin = open('input.txt', 'r')


def findboss(member):
    if lst[member] == 0:
        return member
    ret = findboss(lst[member])
    lst[member] = ret
    return ret

def union(a, b):
    global lst
    a_boss, b_boss = findboss(a), findboss(b)
    if a_boss == b_boss:
        return
    lst[b_boss] = a_boss


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = [0]*200
    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])


    result = [0]*(N+1)
    for i in range(1, N+1):
        if findboss(lst[i]) == 0:
            result[i] = i
        else:
            result[i] = findboss(lst[i])

    cnt_list = []
    for i in range(1, N+1):
        if result[i] not in cnt_list:
            cnt_list.append(result[i])
    print(f'#{tc} {len(cnt_list)}')
