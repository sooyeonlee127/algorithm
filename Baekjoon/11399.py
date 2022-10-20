import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

total = 0
answer = 0
for i in range(N):
    total += arr[i]
    answer += total

print(answer)
