def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,s,t = iim()
w = ii()
ans = 1 if s<=w<=t else 0
for i in range(2,n+1):
    w += ii()
    if s<=w<=t:
        ans += 1
print(ans)