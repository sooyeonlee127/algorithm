def solution(new_id):
    answer = ''
    for id in new_id:
        if ord(id) <= 57 and ord(id) >= 48:
            answer += id
        elif ord(id) <= 90 and ord(id) >= 65:
            answer += chr(ord(id) + 32)
        elif ord(id) >= 97 and ord(id) <= 122:
            answer += id
        elif id == '-' or id == '_':
            answer += id
        elif id == '.' and len(answer) >= 1 and answer[-1] != '.':
            answer += id
            
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[0:len(answer)-1]
        if answer[0] == '.':
            answer = answer[1:len(answer)]
    else:
        answer += 'a'
    
    if len(answer) >= 16:
        answer = answer[0:15]
    if answer[-1] == '.':
        answer = answer[0:len(answer)-1]
    if len(answer) <= 2:
        answer += answer[-1]*(3 - len(answer))
    return answer