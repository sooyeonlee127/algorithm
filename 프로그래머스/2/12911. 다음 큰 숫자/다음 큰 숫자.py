def solution(n):
    answer = 0
    cntN = changeNum(n)
    newN = n + 1
    flag = True
    while  flag:
        if check(cntN, newN):
            answer = newN
            flag = False
        else:
            newN += 1
    return answer


def changeNum(num):
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result

def check(cntN, newN):
    cntNewN = changeNum(newN)
    return cntN.count('1') == cntNewN.count('1')
