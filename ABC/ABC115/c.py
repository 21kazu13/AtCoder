def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,k = iim()
H = []
for _ in range(n):
    H.append(ii())
H.sort()

ans = 1000000000
for i in range(n-k+1):
    ans = min(H[i+k-1]-H[i],ans)
print(ans)