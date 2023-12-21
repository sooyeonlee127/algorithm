answer = 0
def solution(num):
    global answer
    collatz(num, 0)
    return answer

def collatz(num, step):
    global answer
    if num == 1:
        answer = step
        return
    if step >= 500:
        answer = -1
        return
    if num % 2 == 0:
        return collatz(num // 2, step+1)
    else:
        return collatz(num * 3 + 1, step+1)
    
    