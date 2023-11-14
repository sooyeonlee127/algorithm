def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for item in s:
            if ord(item) > 57 or ord(item) < 48:
                answer = False
                break
    else:
        answer = False
    return answer