def solution(triangle):
    answer = []
    for x in range(len(triangle)):
        answer.append([-21e5]*len(triangle[x]))
    answer[0][0] = triangle[0][0]
    for x in range(0, len(triangle)-1):
        for y in range(len(triangle[x])):
            answer[x+1][y] =  max(answer[x][y] + triangle[x+1][y], answer[x+1][y])
            answer[x+1][y+1] =  max(answer[x][y] + triangle[x+1][y+1], answer[x+1][y+1])
    
    return max(answer[-1])