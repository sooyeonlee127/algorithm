def solution(s, n):
    answer = ''

    for st in s:
        num = ord(st)
        if num <= 90 and num >= 65: # 대문자일때
            if num + n > 90:
                answer += chr(num + n - 90 + 64)
            else:
                answer += chr(num+n)
        elif num <= 122 and num >= 97: # 소문자일때
            if num + n > 122:
                answer += chr(num + n - 122 + 96)
            else:
                print(st)
                answer += chr(num+n)
        else:
            answer += st
    return answer