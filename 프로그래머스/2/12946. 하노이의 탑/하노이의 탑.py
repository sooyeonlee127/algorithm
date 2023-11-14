answer = []

def hanoi(N, start, assistant, target):
    global answer
    if N == 1:
        answer.append([start, target])
    else:
        hanoi(N-1, start, target, assistant)
        answer.append([start, target])

        hanoi(N-1, assistant, start, target)


def solution(n):
    global answer
    hanoi(n, 1, 2, 3)
    return answer