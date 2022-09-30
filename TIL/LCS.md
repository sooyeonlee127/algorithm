LCS는 두 가지로 나뉜다.  
S가 string, Subsquance라는 차이가 있다.

차이점은 '끊기지 않고 연속되었는가, 연속되지 않았는가.'의 차이이다.

-   LCS(String): 중간에 끊기지 않고 연속되어야 한다.
-   LCS(Subsquance): 연속되지 않아도 된다. 중간에 끊겨도 된다.

# LCS(String)

longest common **string**  
최장공통부분 문자열

DP로 풀이한다.



### 코드(python)

```
word1 = 'BABJYP'
word2 = 'ABCBJY'
N = len(word1)
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if word1[i-1] == word2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
MAX = 0
for i in range(N+1):
    for j in range(N+1):
        if MAX < arr[i][j]:
            MAX = arr[i][j]

print(MAX)
```

핵심: 같으면 11시 값 + 1을 해주고, 다르다면 0을 해준다.



---
# LCS(Subsquance)

longest common **subsequance**  
최장공통부분수열

DP로 풀이한다.



### 코드(python)

```
word1 = 'BABJYP'
word2 = 'ABCBJY'
N = len(word1)
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if word1[i-1] == word2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

MAX = 0
for i in range(N+1):
    for j in range(N+1):
        if MAX < arr[i][j]:
            MAX = arr[i][j]

print(MAX)
```

핵심: 같으면 11시 값 + 1을 해주고, 다르면 위, 왼쪽 중 최대값을 넣어준다.

LCS(Stirng)과 차이는 이 코드를 추가한 것밖에 없다.

```
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
```