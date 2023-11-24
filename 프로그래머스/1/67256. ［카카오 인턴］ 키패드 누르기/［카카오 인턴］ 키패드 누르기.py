
from collections import deque

def solution(numbers, hand):
    answer = ''
    board = [[1,2,3],[4,5,6],[7,8,9],['*',0, '#']]
    board_dict = dict()

    for i in range(4):
        for j in range(3):
            board_dict[board[i][j]] = [i,j]
    left = board_dict['*']
    right = board_dict['#']
    for number in numbers:
        if board_dict[number][1] == 0:
            answer += 'L'
            left = board_dict[number]
        elif board_dict[number][1] == 2:
            answer += 'R'
            right = board_dict[number]
        else:
            right_cnt = bfs(right[0], right[1], [[0]*3 for _ in range(4)], number, board)
            left_cnt = bfs(left[0], left[1], [[0]*3 for _ in range(4)], number, board)
            if right_cnt > left_cnt:
                answer += 'L'
                left = board_dict[number]
            elif right_cnt < left_cnt:
                answer += 'R'
                right = board_dict[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = board_dict[number]
                else:
                    answer += 'L'
                    left = board_dict[number]
                    
    return answer
            
        
        
        
def bfs(sy,sx,used,target, board):
    if board[sy][sx] == target:
        return 0
    direct_y = [-1,1,0,0]
    direct_x = [0,0,-1,1]
    used[sy][sx] = 1
    q = deque()
    q.append([sy, sx, 0])
    while q:
        y,x,cnt = q.popleft()
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if dy < 0 or dy >= 4 or dx < 0 or dx >= 3: continue
            if board[dy][dx] == target:
                return cnt+1
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy,dx,cnt+1])