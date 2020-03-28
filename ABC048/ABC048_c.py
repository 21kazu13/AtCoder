n, x = map(int,input().split())
A = list(map(int,input().split()))
if A[0] > x:
    ans = A[0] - x
    A[0] -= ans
else:
    ans = 0
for j in range(n):
    if j != n-1:
        if A[j]+A[j+1]> x:
            diff = A[j+1]+A[j]-x
            ans += diff
            if A[j+1] - diff > 0:
                A[j+1] -= diff
            else:
                A[j+1] = 0
    else:
        if A[j]> x:
            diff = A[j]-x
            ans += diff
print(ans)