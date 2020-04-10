def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
B = iil()
ans = 0
for i in range(1,n-1):
    ans += min(B[i-1],B[i])
print(ans+B[0]+B[-1])