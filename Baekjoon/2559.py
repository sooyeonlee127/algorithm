N, K = map(int, input().split())
temp = list(map(int, input().split()))
total = 0
MAX = -21e8

for i in range(K): # 초기값 설정(처음 구간만큼 더해놓는다)
    total += temp[i]

for i in range(N-K+1):
    if total > MAX: # 최대값일 경우 경신해준다.
        MAX = total
    if i == N-K: break
    total += temp[i+K] # 다음 구간의 마지막 인덱스를 추가해주고
    total -= temp[i] # 이전 구간의 처음 인덱스를 빼준다.

print(MAX)
