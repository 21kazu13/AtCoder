def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,t = iim()
ans = 0
A = []
for i in range(n):
    A.append(ii())

for i in range(1,n):
    ans += min(t,A[i]-A[i-1])
print(ans+t)