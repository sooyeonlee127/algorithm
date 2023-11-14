answer = 0

def check(num):
    global answer
    if num == 1:
        return
    answer += 1

    if answer > 500:
        answer = -1
        return
    if num % 2 == 0:
        return check(num//2)
    else:
        return check((num*3)+1)
def solution(num):
    global answer
    if num == 1:
        answer = 0
    else:
        check(num)
    return answer