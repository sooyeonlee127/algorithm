zero = 0
check = 1

def translation(num):
    global zero, check
    check += 1
    result = ''
    while num:
        temp = num % 2
        if temp == 1:        
            result += '1'
        else:
            zero += 1
        num //= 2
    return result
        

def solution(s):
    global zero
    answer = []
    zero += s.count('0')
    string = s.replace('0', '')

    while string != '1':
        string = translation(len(string))
    answer = [check, zero]
    return answer