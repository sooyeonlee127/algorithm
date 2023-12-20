def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    while progresses:
        tmp = 0
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            tmp += 1
        if tmp > 0:
            answer.append(tmp)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

    return answer