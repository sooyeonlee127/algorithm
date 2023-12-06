



def solution(rows, columns, queries):
    answer = []
    arr = []
    num = 1
    for row in range(rows):
        temp = []
        for col in range(columns):
            temp.append(num)
            num+=1
        arr.append(temp)
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        backup = arr[x1][y1]
        MIN = backup
        for i in range(x1, x2):
            arr[i][y1] = arr[i+1][y1]
            MIN = min(MIN, arr[i+1][y1])
        for j in range(y1, y2):
            arr[x2][j] = arr[x2][j+1]
            MIN = min(MIN, arr[x2][j+1])
        for i in range(x2,x1,-1):
            arr[i][y2] = arr[i-1][y2]
            MIN = min(MIN, arr[i-1][y2])
        for j in range(y2, y1+1, -1):
            arr[x1][j] = arr[x1][j-1]
            MIN = min(MIN, arr[x1][j-1])
        arr[x1][y1+1] = backup
        answer.append(MIN)

    
        
    return answer