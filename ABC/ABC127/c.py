def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
lmax = 0
rmin = n
for i in range(m):
    l,r = iim()
    lmax = max(l,lmax)
    rmin = min(r,rmin)

print(max(rmin-lmax+1,0))