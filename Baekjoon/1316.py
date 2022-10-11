n = int(input())
for test_case in range(1, n+1):
    text = input()
    for i in range(0, len(text)-1):
        if text[i] == text[i+1] :
            pass
        elif text[i] in text [i+1:] :
            n -= 1
            break
print(n)


