alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
h,w = map(int,input().split())
for i in range(h):
    A = list(map(str,input().split()))
    for j in range(w):
        if A[j] == 'snuke':
            ans = alpha[j]+str(i+1)
print(ans)