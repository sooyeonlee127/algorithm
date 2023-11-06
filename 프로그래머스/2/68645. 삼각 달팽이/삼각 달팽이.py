from collections import deque

def solution(n):
    left_list = [deque() for _ in range(n)]
    right_list = [deque() for _ in range(n)]
    answer = []
    start = 0
    end = n - 1
    num = 1
    while end >= start:
        for i in range(start, end + 1):
            if i == end:
                for j in range(end + 1 - len(left_list[i]) - len(right_list[i])):
                    left_list[i].append(num)
                    num += 1
                end -= 1
            else:
                left_list[i].append(num)
                num += 1
        start += 1
        for i in range(end, start-1, -1):
            right_list[i].appendleft(num)
            num += 1
        start += 1
    for i in range(n):
        left = len(left_list[i])
        right = len(right_list[i])
        for l in range(left):
            answer.append(left_list[i].popleft())
        for r in range(right):
            answer.append(right_list[i].popleft())
    return answer