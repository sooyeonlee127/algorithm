answer = 0
cnt = 0
lst = ['A', 'E', 'I', 'O', 'U']
def check(w, target):
    global answer, cnt
    if w == target:
        answer = cnt
        return
    if len(w) == 5:
        return
    for i in lst:
        cnt += 1
        check(w+i, target)
    

def solution(word):
    global answer
    check('', word)
    return answer