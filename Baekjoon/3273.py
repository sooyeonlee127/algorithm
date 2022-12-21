N = int(input())
arr = list(map(int, input().split()))
target = int(input())
arr.sort() # 리스트를 정렬해준다.
cnt = 0
total = 0
low = 0 # 처음 인덱스
high = N-1 # 마지막 인덱스

while high > low: # 투포인터의 위치가 바뀌지 않을 때만 동작
    total = arr[low] + arr[high]
    if total < target: # 목표값보다 작을 때
        low += 1 # 작은 인덱스를 키워준다
    elif total == target: # 목표값을 찾을 때마다 수를 세어준다
        cnt += 1
        low += 1
    else: # 목표값보다 클 때
        high -= 1 # 큰 인덱스를 줄여준다

print(cnt)
