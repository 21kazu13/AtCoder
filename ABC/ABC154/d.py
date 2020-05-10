def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,k = iim()
P = iil()
Psum = []
tmp = 0
for i in P:
    tmp += i
    Psum.append(tmp)

ans = Psum[k-1]
for i in range(1,n-k+1):
    ans = max(ans,Psum[i+k-1]-Psum[i-1])

print((ans+k)/2)