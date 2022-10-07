빠른 검색을 위해 **HASH**(O(1)의 속도)와 **BST**(O(logn)의 속도)를 많이 사용함

HASH는 DAT 자료구조의 단점을 보완할 수 있는 자료구조이다.

---

## DAT 자료구조

: n개의 정수를 입력 받은 후, (예. 3 2 7 5 1 4)

  숫자 1개 입력(m) (예. 6)

  숫자 m이 몇개 입력이 되었는지 확인하는 코드.

    0     1      2      3      4      5      6     7      8

| 0 | 1 | 1 | 1 | 1 | 1 | **0** | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### 단점

:배열을 숫자의 크기만큼 만들어야함

음수인 경우 처리가 어려움

문자열인 경우 어려움

→ DAT의 단점을 HASH로 해결할 수 있다.

: hashf()하여 return한 값을 DAT하여 해결한다.

1\. 원본데이터 값: key값

2\. hashf(key) -> return key + 10

3\. DAT

만약, return (key + 10) % 3 과 같은 return을 해서 중복값이 된다면,

open adressing을 해서 해결



자료를 저장하는 방식은 언어마다 다르다.

저장이 잘못될 경우 속도가 느려지기 때문에, 균형을 맞춰주는 게 중요하다.

Channing - 링크드리스트(연결 리스트): balanced tree(red-blacktree) - 균형을 맞춰주는 방식

Open Adressing - 더블 hash, 리니어

---

#### python으로 hash를 쓸 때, 자주 사용하는 모듈 Counter

```
from collections import Counter
```
