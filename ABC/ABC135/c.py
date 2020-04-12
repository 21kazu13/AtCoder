def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
B = iil()
rep = 0
ans = 0
for i,item in enumerate(B):
    ans += min(A[i],item+rep)
    rep = max(0, item - max(0, A[i] - rep))
print(ans+min(A[-1],rep))