def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
P = iil()
ans = 0
for i in range(1,n-1):
    if (P[i-1] < P[i] < P[i+1]) or (P[i+1] < P[i] < P[i-1]):
        ans += 1
print(ans)