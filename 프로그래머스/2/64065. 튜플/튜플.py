def solution(s):
    answer = []
    check = dict()
    num = ''
    for n in s:
        if n  == '{' or n == '}' or n == ',':
            if len(num) > 0:
                if check.get(num):
                    check[num] += 1
                else:
                    check[num] = 1
                num = ''
        else:
            num += n
    check = sorted(check.items(), key=lambda x: -x[1])
    for i in range(len(check)):
        answer.append(int(check[i][0]))
    return answer