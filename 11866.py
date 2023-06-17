from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

q = deque()
N, K = map(int, sys.stdin.readline().rstrip().split())

for num in range(1, N+1):
    q.append(num)

print("<", end="")
while len(q)>1:
    for i in range(K-1):
        q.append(q.popleft())
    print(q.popleft(), end=", ")

print(q[0], end=">")
