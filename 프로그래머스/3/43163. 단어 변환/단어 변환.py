from collections import deque

    
def solution(begin, target, words):
    if target not in words: return 0
    answer = 0
    used = [0]*len(words)
    q = deque()
    q.append([begin, 0])
    while q:
        word, cnt = q.popleft()
        if word == target: return cnt
    
        for i in range(len(words)):
            if not used[i]:
                if sum(x != y for x,y in zip(word, words[i])) == 1:
                    q.append([words[i], cnt+1])
                    used[i] = 1
    return 0

    
