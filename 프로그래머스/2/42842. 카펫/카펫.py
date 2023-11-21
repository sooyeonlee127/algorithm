def solution(brown, yellow):
    answer = []
    for num in range(1, yellow+1):
        if yellow % num != 0: continue
        if brown == (yellow//num) * 2 + (num *2) + 4:
            answer = [yellow//num+2,num+2]
            break        
    return answer