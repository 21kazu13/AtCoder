def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
H = iil()
d = {}
for i in range(m):
    a,b = iim()
    d[a] = max(d.get(a,0),H[b-1])
    d[b] = max(d.get(b,0),H[a-1])
ans = 0
for i,item in enumerate(H):
    if item > d.get(i+1,0):
        ans += 1
print(ans)