def solution(n):
    answer = 0
    lst = []
    while n:
        lst.append(n%3)
        n //= 3
    lst.reverse()
    for i in range(len(lst)):
        answer += lst[i] * (3 ** i) 
    return answer