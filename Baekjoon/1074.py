N, r, c = map(int, input().split())
total = 0

def number(N, r, c):
    global total
    if N == 0: return
    m = 2**(N-1)
    if r < m and c < m:
        pass
    elif r < m and c >= m:
        total += m**2
    elif r >= m and c < m:
        total += m**2*2
    else:
        total += m**2*3
    
    number(N-1, r%m, c%m)

number(N, r, c)
print(total)
