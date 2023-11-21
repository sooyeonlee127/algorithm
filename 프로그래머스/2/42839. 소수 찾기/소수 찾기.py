from itertools import permutations

def solution(numbers):
    answer = []
    num = []
    for i in range(1, len(numbers)+1):
        num.append(list(permutations(numbers, i)))
    num = [int(''.join(y)) for x in num for y in x]
    for i in num:
        if check(i):
            answer.append(i)
    return len(set(answer))



def check(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    