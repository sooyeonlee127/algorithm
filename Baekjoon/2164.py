from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

q = deque()
N = int(sys.stdin.readline())
for num in range(1, N+1):
    q.append(num)

while True:
    q.popleft()
    if len(q) == 1:
        break
    q.rotate(-1)

print(q[0])
