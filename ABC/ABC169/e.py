def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))


n = ii()
A = []
B = []

for _ in range(n):
    a,b = iim()
    A.append(a)
    B.append(b)
A.sort()
B.sort()

if n%2 == 1:
    ans = B[n//2]-A[n//2]+1
else:
    lmin = A[n//2-1]
    lmax = B[n//2-1]
    rmin = A[n//2]
    rmax = B[n//2]
    ans = (rmax+lmax) - (rmin+lmin) + 1
print(ans)