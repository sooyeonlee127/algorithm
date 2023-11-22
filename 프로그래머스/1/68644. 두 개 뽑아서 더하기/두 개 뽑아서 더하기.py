def solution(numbers):
    answer = []
    sum_lst = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            sum_lst.append(numbers[i]+numbers[j])
    sum_lst = list(set(sum_lst))
    sum_lst.sort()
    return sum_lst