def bit_print(i): # 3번비트부터 0번비트 출력
    s = ''
    for j in range(3, -1, -1): # i의 j번째 비트가 1인지 판별
        s += '1' if (i&(1<<j)) else '0' # 1이면 1, 0이면 0 리턴
    return s


T = int(input())

for tc in range(1, T+1):
    n, num = input().split()
    n = int(n)
    tmp = ''
    for i in range(n):
        if num[i].isalpha(): # 알파벳일 경우 숫자로 변환
            tmp += bit_print(ord(num[i])-55) # A: 10 ~
        else:
            tmp += bit_print(int(num[i]))
    print(f'#{tc} {tmp}')
