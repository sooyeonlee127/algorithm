from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for w, l in results:
        win[l].add(w) # l한테 이긴 사람들 배열
        lose[w].add(l) # w한테 진 사람들 배열
    for i in range(1, n+1):
        for w in win[i]: # i를 이긴 사람들
            lose[w].update(lose[i])
            # i를 이긴 w는 i한테 진 사람들을 모두 이김
        for l in lose[i]: # i한테 진 사람들
            win[l].update(win[i])
            # i한테 진 l은 i를 이긴 사람한테 모두 짐

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
    return answer