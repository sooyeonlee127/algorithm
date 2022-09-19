def bit_print(num):
    result = ''
    while len(result) < 13: # 13자리 이상이면 overflow로 끝낸다.
        num *= 2 # 소수계산 일 때는 2**(-1) 로 나누어 준다 == 2를 곱한다
        s = str(num).split(".") # 결과 값에서 몫과 나머지를 나누어줌
        result += s[0] # 몫을 결과값에 추가해줌

        if s[1] == '0': # 나머지가 0이면
            return result # 리턴
        # 나머지가 0이 아니라면,
        num = float('0.' + s[1]) # 다시 실수 형태로 바꾸어서 반복문을 돈다
    return 'overflow' # 13자리 이상이면 'overflow' 출력

T = int(input())

for tc in range(1, T+1):
    n = float(input()) # 0보다 크고 1미만인 십진수 n
    print(f'#{tc} {bit_print(n)}')