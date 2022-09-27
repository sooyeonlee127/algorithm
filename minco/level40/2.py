import sys
sys.stdin = open('input.txt', 'r')

def abc(num):
    if num >= 2:
        return abc(num-1) + abc(num-2)
    else:
        return num

N = int(input())
print(abc(N+1))

