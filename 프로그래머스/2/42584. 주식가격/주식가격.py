def solution(prices):
    answer = [0]*len(prices)
    stack = []    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    for s in stack:
        answer[s] = len(prices) - s - 1
    return answer