
def solution(numbers):
    answer = ''
    str_numbers = list(map(str, numbers))
    str_numbers = sorted(str_numbers, key=lambda x: x*3, reverse=True)

    return str(int(''.join(str_numbers)))