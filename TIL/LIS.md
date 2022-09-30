# LIS

Longest increasing subsequence  
최장공통부분수열

dp로 풀이한다.



### 코드

```
arr = [10,20,10,30,20,50]
N = len(arr)
result = [1]*N
# 큰 값이 하나도 없다고 하더라도 LIS는 1이기 때문에 초기값으로 1을 넣어준다.

for i in range(N):
    for j in range(0, i):
            # 앞의 값 > 뒤의 값
        if arr[i] > arr[j]:
            result[i] = max(result[j]+1, result[i])
print(max(result))
```

핵심: 비교대상의 값이 더 작을 경우, '비교대상의 result값 + 1'과 '현재의 result값'을 비교하여 큰 값을 넣는다.