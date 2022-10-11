T = int(input())

for tc in range(1, T+1):
    arr = input()
    stack = []
    flag = 1
    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
        else:
            if len(stack) > 0:
                stack.pop()
            elif len(stack) == 0:
                flag = 0
                break

    if len(stack) > 0:
        flag = 0

    if flag:
        print('YES')
    else:
        print('NO')
