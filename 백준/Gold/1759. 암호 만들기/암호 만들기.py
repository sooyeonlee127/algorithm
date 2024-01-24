from itertools import combinations

L, C = map(int, input().split())
STR = list(map(str, input().split()))
test = list(combinations(STR, L))
result = []
for T in test:
    m_cnt = 0
    if 'a' in T: m_cnt += 1
    if 'e' in T: m_cnt += 1
    if 'i' in T: m_cnt += 1
    if 'o' in T: m_cnt += 1
    if 'u' in T: m_cnt += 1
    if m_cnt >= 1 and L - m_cnt >= 2:
        result.append(sorted(list(T)))


answer = sorted(result)
for ans in answer:
    print(''.join(ans))

    