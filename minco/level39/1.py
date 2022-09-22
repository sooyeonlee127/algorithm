arr = list(map(int, input().split()))
arr.sort()
n = len(arr)
result = 0
for i in range(n, 0, -1):
    result += arr[n-i]*(i-1)
print(result)