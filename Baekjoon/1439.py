import sys
sys.stdin = open('input.txt', 'r')


arr = input()
bucket = [0]*2

start = 0
lst = []

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        lst.append(arr[start:i+1])
        start = i+1

lst.append(arr[start:])

for i in range(len(lst)):
    bucket[int(lst[i][0])] += 1

print(min(bucket))