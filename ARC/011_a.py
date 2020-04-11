def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

m,n,N = iim()
ans = N
mod = 0
ret = N + mod#next source
while ret >= m:
    ret = N + mod#next source
    N = (ret // m) * n
    ans += N
    mod = ret % m#next store
#    print(ret,N,mod,ans)
print(ans)
