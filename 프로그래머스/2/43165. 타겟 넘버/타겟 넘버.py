answer = 0

def solution(numbers, target):
    global answer    
    dfs(0,0, numbers, target)
    return answer

def dfs(level, total, numbers, target):
    global answer    

    if level == len(numbers):
        if total == target:
            answer += 1
        return
    lst = [1,-1]
    for i in lst:
        dfs(level+1, total+numbers[level]*i, numbers, target)
            
        
        
        
    