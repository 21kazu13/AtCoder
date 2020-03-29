def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
ans = 0
n = ii()

for i in range(n):
    x,u = ism()
    if u == 'JPY':
        ans += int(x)
    else:
        ans += float(x)*380000
print(ans)