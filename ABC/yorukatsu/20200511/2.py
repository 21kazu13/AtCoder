def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n,k = iim()
h = []
for _ in range(n):
    h.append(ii())
h.sort()

ans = float('INF')
for i in range(n-k+1):
#    print(i,i+k-1,h[i],h[i+k-1])
    ans = min(ans,h[i+k-1]-h[i])
print(ans)