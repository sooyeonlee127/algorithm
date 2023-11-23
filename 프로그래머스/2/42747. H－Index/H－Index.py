def solution(citations):
    answer = 0
    citations.sort()
    for (idx, h) in enumerate(citations):
        for i in range(h+1):
            if len(citations) - idx >= i:
                answer = max(answer, i)
    return answer