from itertools import permutations

N = int(input())
MAP = list(map(int,input().split()))
lst = list(permutations(MAP, N))
MAX = -21
for arr in lst:
    result = 0
    for i in range(N-1):
        result += abs(arr[i] - arr[i+1])
    MAX = max(MAX, result)
print(MAX)
