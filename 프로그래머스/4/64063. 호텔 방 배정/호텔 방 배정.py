import sys
sys.setrecursionlimit(2000)

def solution(k, room_number):
    check_in = dict()
    for num in room_number:
        check(num, check_in)
    return list(check_in)



def check(num, check_in):
    if num not in check_in:
        check_in[num] = num + 1
        return num
    else:
        empty = check(check_in[num], check_in)
        check_in[num] = empty + 1
        return empty
        
        
    
    