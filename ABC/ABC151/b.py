def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n,k,m = iim()
A = iil()
if m*n - sum(A) > k:
    print(-1)
else:
    print(max(m*n - sum(A),0))
