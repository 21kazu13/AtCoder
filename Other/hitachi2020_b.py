def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
a,b,m = iim()
A = iil()
B = iil()
ans = min(A)+min(B)

for i in range(m):
    x,y,c = iim()
    ans = min(ans,A[x-1]+B[y-1]-c)
print(ans)