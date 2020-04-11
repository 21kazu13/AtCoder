def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
ans = 0
for i,item in enumerate(A):
    ans += (2**(n-i-1))*item
print(ans)