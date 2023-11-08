



def solution(rows, columns, queries):
    answer = []
    MAP = [[(i)*columns+(j+1) for j in range(columns)] for i in range(rows)]
    num = 1

    for x1,y1,x2,y2 in queries:
        MIN = 21e5
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        backup = MAP[x1][y1]
        MIN = min(MIN, backup)
        for i in range(x1,x2):
            MAP[i][y1] = MAP[i+1][y1]
            MIN = min(MIN, MAP[i+1][y1])
            
        for i in range(y1, y2):
            MAP[x2][i] = MAP[x2][i+1]
            MIN = min(MIN, MAP[x2][i+1])
            
        for i in range(x2, x1, -1):
            MAP[i][y2] = MAP[i-1][y2]
            MIN = min(MIN, MAP[i-1][y2])
            
        for i in range(y2, y1, -1):
            MAP[x1][i] = MAP[x1][i-1]
            MIN = min(MIN, MAP[x1][i-1])
            

        MAP[x1][y1+1] = backup
        answer.append(MIN)
    
    return answer