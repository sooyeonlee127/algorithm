import sys
sys.stdin = open('input.txt', 'r')



T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 종이의 개수, M: 순서를 알고 싶은 종이번호
    arr = list(map(int, input().split())) # 종이의 가중치
    result = [] # 출력 순서를 담을 배열

    lst = []  # 새롭게 만들 배열 [가중치, 종이번호]의 형식으로 채울 것
    for i in range(N):
        lst.append([arr[i], i])

    while lst: # lst가 빌 때까지 반복
        tmp = lst.pop(0) # 선입선출
        standard = tmp[0] # 가중치
        result.append(tmp[1]) # 종이번호
        length = len(lst) # 남은 종이의 수

        for i in range(length):
            if lst[i][0] > standard: # 가중치가 높은 게 있다면
                back = result.pop() # 결과값에서 빼고
                lst.append([standard, back]) # 가장 뒤로 보낸다
                break

    print(result.index(M)+1)

