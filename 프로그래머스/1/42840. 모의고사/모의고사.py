

def solution(answers):
    answer = []
    stu1 = [1,2,3,4,5]*8
    stu2 = [2,1,2,3,2,4,2,5] * 5
    stu3 = [3,3,1,1,2,2,4,4,5,5] * 4
    score1 = 0
    score2 = 0
    score3 = 0
    idx = 0
    for i in range(len(answers)):
        if stu1[i%40] == answers[i]:
            score1 += 1
        if stu2[i%40] == answers[i]:
            score2 += 1
        if stu3[i%40] == answers[i]:
            score3 += 1

    MAX = max(score1, score2, score3)
    lst = [score1, score2, score3]
    for i in range(3):
        if MAX == lst[i]:
            answer.append(i+1)
    return answer