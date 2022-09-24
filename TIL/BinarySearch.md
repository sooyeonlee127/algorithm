# 이진탐색
: 탐색방법의 일종이다.

binary search != binary search tree (binary search tree는 자료구조이다)



시간복잡도: O(logn)

정렬되어있는 상태에서만 사용이 가능하다. 정렬되어있지 않으면 정렬부터 해야한다.



### 예시
정수 개수 : n

정수 : [1, 3, 5, 7, 9, 13, 16]

target : 6

start index: 0

end index: n-1

mid index: n // 2

만약 mid index 보다 크면, start를 mid + 1로 옮김

만약 mid index 보다 작으면, end를 mid -1로 옮김

start와 end의 순서가 바뀌면 (end < start) 찾고자 하는 값이 없는 것이다.



### 코드
```
n=int(input())
arr=list(map(int,input().split()))
target=int(input())


def binary_search(st,ed,value):
    while (1):
        mid=(st+ed)//2          # 미드값 찾기
        if arr[mid]==value:     # 찾을경우
            return 1
        elif arr[mid] > value:  # 찾고자 하는 값이 더 작으면
            ed=mid-1
        elif arr[mid]<value:    # 찾고자 하는 값이 미드값 보다 더 크면
            st=mid+1
        if st>ed:               # st index와 ed index 가 교차되면... 없는 숫자
            return 0
        
arr.sort()
ret=binary_search(0,n-1,target)
if ret:
    print("찾음")
else:
    print("없는 숫자")
```