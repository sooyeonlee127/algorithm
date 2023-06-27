from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    func = list(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline())
    ls = sys.stdin.readline().rstrip()
    if ls != '[]':
        ls = ls[1:-1]
        q = deque(list(map(int, ls.split(','))))
    else:
        q = deque([])
    pointer = True
    answer = ''
    if func.count('D') > 0 and func.count('D') > len(q):
        answer = 'error'
    else:
        for f in func:
            if f == 'D':
                if len(q) == 0:
                    answer = 'error'
                    break
                if pointer:
                    q.popleft()
                else:
                    q.pop()
            else:
                pointer = not(pointer)
    if answer:
        print(answer)
    else:
        if len(q) == 0:
            print('[]')
        elif pointer:
            print('[', end='')
            for i in range(len(q)-1):
                print(q[i], end=',')
            print(q[-1], end=']')
            print()
        else:
            print('[', end='')
            for i in range(len(q)-1, 0, -1):
                print(q[i], end=',')
            print(q[0], end=']')
            print()
