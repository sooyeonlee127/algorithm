def preorder(now):
    if now:
        print(chr(now+64), end='')
        preorder(ch1[now])
        preorder(ch2[now])

def inorder(now):
    if now:
        inorder(ch1[now])
        print(chr(now+64), end='')
        inorder(ch2[now])


def postorder(now):
    if now:
        postorder(ch1[now])
        postorder(ch2[now])
        print(chr(now+64), end='')



N = int(input())
arr = [list(input().split()) for _ in range(N)]
V = N+1
root = 1


ch1 = [0]*(N+1)
ch2 = [0]*(N+1)
for i in range(N):
    p, c1, c2 = ord(arr[i][0]) - 64, ord(arr[i][1]) - 64, ord(arr[i][2]) - 64
    if c1 != -18:
        ch1[p] = c1
    if c2 != -18:
        ch2[p] = c2


preorder(root)
print()
inorder(root)
print()
postorder(root)
