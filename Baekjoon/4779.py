def func(level, now):
    # print(level, now)
    if level == 2:
        print(' '*now, end="")
        return

    if now == 1:
        print('-', end="")
        return

    for i in range(3):
        func(i+1, now//3)

flag = True
while flag:
    try:
        N = int(input())
        func(0, 3**N)
        print()

    except:
        flag = False
