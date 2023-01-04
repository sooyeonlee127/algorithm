N, M = map(int, input().split())

arr = [input() for _ in range(N+M)] # 듣도 못한 배열과 보도 못한 배열을 함께 받음
set_arr = set(arr) # 중복제거

arr.sort() # 듣도 보도 못한 리스트 정렬

result = len(arr)-len(set_arr) # 듣도 보도 못한 개수

print(result)

for i in range(N+M-1):
    if arr[i] == arr[i+1]:
        print(arr[i])
