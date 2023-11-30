def solution(p):
    answer = ''
    answer = step(p)
    return answer

def checkBalance(string):
    lst = list(string)
    openCnt = lst.count('(')
    closeCnt = lst.count(')')
    return openCnt == closeCnt

def checkRight(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True

def changeV(v):
    newString = '('
    ret = step(v)
    newString += ret
    newString += ')'
    return newString

def reverseU(u):
    newString = ''
    for i in range(1, len(u)-1):
        if u[i] == '(':
            newString += ')'
        else:
            newString += '('
    return newString
    


def step(string):
    if string == '':
        return string
    if checkRight(string):
        return string
    u = ''
    v = ''
    for i in range(1, len(string), 2):
        if checkBalance(string[0:i+1]):
            u = string[0:i+1]
            v = string[i+1:]
            break
    # u가 올바른 괄호문자열인 경우
    if checkRight(u):
        ret = step(v)
        return u + ret
    # u가 올바른 괄호문자열이 아닌 경우
    else:
        newV = changeV(v)
        newU = reverseU(u)
        return newV + newU 
