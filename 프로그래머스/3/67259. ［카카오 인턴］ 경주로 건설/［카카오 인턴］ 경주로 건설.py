from collections import deque
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1: board[i][j] = -1
    
    def bfs(sy,sx, path, board):
        size = len(board)
        arr = [[0]*size for _ in range(size) ]
        direct = [(-1,0), (1,0), (0,-1), (0,1)]
        q = deque()
        q.append([sy, sx, 0, path])
        while q:
            y, x, cost, path = q.popleft()
            for i in range(4):
                dy = y + direct[i][0]
                dx = x + direct[i][1]
                if dy < 0 or dy >= size or dx < 0 or dx >= size: continue
                if board[dy][dx] == -1: continue
                new_cost = 0
                if path == i: new_cost = cost + 100
                else: new_cost = cost + 600
                if arr[dy][dx] == 0 or (arr[dy][dx] != 0 and arr[dy][dx] > new_cost):
                    q.append([dy,dx,new_cost,i])
                    arr[dy][dx] = new_cost
        return arr[size-1][size-1]
    
    answer = min(bfs(0,0,1,board), bfs(0,0,3,board))

    

    return answer