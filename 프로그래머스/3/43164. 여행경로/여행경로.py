answer = []

def solution(tickets):
    global answer
    dfs( ['ICN'], tickets, [0]*len(tickets))
    answer.sort()
    answer = answer[0]
    return answer

def dfs(result, tickets, used):
    global answer
    if len(result) == len(tickets)+1:
        answer.append(result[:])
        return 
    
    for t in range(len(tickets)):
        if tickets[t][0] != result[-1]: continue
        if used[t] == 1: continue
        used[t] = 1
        result.append(tickets[t][1])
        dfs(result, tickets, used)
        used[t] = 0
        result.pop()
            
    
    