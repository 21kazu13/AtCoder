def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n,k = iim()
ans = 0
mod = 1000000007
for i in range(k,n+2):
    ans += n*(n+1)//2 - i*(i-1)//2 - (n-i)*(n-i+1)//2 + 1
    ans = ans%mod

print(ans)