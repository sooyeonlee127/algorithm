## Anagram

: 단어나 문장을 구성하고 있는 문자의 순서를 바꾸어 다른 단어나 문장을 만드는 것

예) wolf, flow

#### \[예제\] Anagram 인지 확인하시오

```
arr1 = input()
arr2 = input()
board1 = [0]*26
board2 = [0]*26
for i in (arr1):
    board1[ord(i)-ord('a')]+=1
for i in (arr2):
    board2[ord(i) - ord('a')] += 1
    
flag=1
for i in range(26):
    if board1[i]!=board2[i]:
        flag=0
        break
if flag:
    print('anagram')
else:
    print('anagram 아님')
```

```
vect1=input()
vect2=input()
if sorted(vect1)==sorted(vect2):
    print('anagram')
else: print('anagram')
```

#### \[예제\] anagram이 아닐 시 몇 개의 문자를 삭제해야 하는가

```
arr1 = input()
arr2 = input()

board1 = [0]*30
board2 = [0]*30

for i in arr1:
    board1[ord(i)-ord('a')] += 1
for i in arr2:
    board2[ord(i)-ord('a')] += 1
cnt = 0
for i in range(30):
    if board1[i] != board2[i]:
        cnt += abs(board1[i] - board2[i])

print(cnt)
```